# Sports Academy Court Booking Calendar System
## Comprehensive Architectural Analysis

---

## 1. EXECUTIVE SUMMARY

This document provides a detailed architectural blueprint for the Sports Academy Court Booking Calendar System based on the provided BRD. The system is a full-stack web application requiring robust database design, microservices architecture, and real-time synchronization capabilities.

**Key Challenges:**
- Real-time double-booking prevention
- Complex booking rules (ping pong logic, cricket net logic)
- Multi-tenant court management
- Concurrent user access handling
- Payment gateway integration
- Notification system reliability

---

## 2. DATABASE DESIGN (RELATIONAL MODEL - PostgreSQL)

### 2.1 Core Tables

#### **Users Table**
```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    user_type ENUM('PLAYER', 'COACH', 'ADMIN') NOT NULL,
    status ENUM('ACTIVE', 'INACTIVE', 'SUSPENDED') DEFAULT 'ACTIVE',
    profile_picture_url TEXT,
    emergency_contact_name VARCHAR(255),
    emergency_contact_phone VARCHAR(20),
    liability_form_signed BOOLEAN DEFAULT FALSE,
    liability_form_signed_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_phone ON users(phone_number);
```

#### **Courts/Nets/Tables Inventory**
```sql
CREATE TABLE court_types (
    court_type_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type_name VARCHAR(100) NOT NULL, -- 'Indoor Court', 'Outdoor Court', 'Ping Pong Table', 'Cricket Net'
    description TEXT,
    capacity INT NOT NULL, -- max players
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courts (
    court_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    court_type_id UUID NOT NULL REFERENCES court_types(court_type_id),
    court_number VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255),
    location VARCHAR(255),
    is_indoor BOOLEAN NOT NULL,
    capacity INT NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    status ENUM('AVAILABLE', 'MAINTENANCE', 'BLOCKED') DEFAULT 'AVAILABLE',
    maintenance_until TIMESTAMP,
    blocked_reason TEXT,
    sports_supported JSON, -- ['Badminton', 'Pickleball', 'Cricket', 'Ping Pong']
    special_rules JSON, -- Court-specific rules
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cricket_nets (
    net_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    net_number VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255),
    location VARCHAR(255),
    capacity INT NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    status ENUM('AVAILABLE', 'MAINTENANCE', 'BLOCKED') DEFAULT 'AVAILABLE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ping_pong_tables (
    table_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_number VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255),
    location VARCHAR(255),
    capacity INT NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    status ENUM('AVAILABLE', 'MAINTENANCE', 'BLOCKED') DEFAULT 'AVAILABLE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_courts_status ON courts(status);
CREATE INDEX idx_courts_type ON courts(court_type_id);
```

#### **Sports Master Data**
```sql
CREATE TABLE sports (
    sport_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sport_name VARCHAR(100) NOT NULL UNIQUE, -- Badminton, Pickleball, Cricket, Ping Pong
    description TEXT,
    min_players INT,
    max_players INT,
    skill_levels JSON, -- ['BEGINNER', 'INTERMEDIATE', 'ADVANCED']
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **Booking Master Configuration**
```sql
CREATE TABLE booking_configurations (
    config_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    config_name VARCHAR(100) NOT NULL,
    time_slot_options JSON, -- [30, 60, 120] minutes
    default_slot_duration INT DEFAULT 60, -- in minutes
    max_booking_duration_per_day INT DEFAULT 480, -- in minutes
    max_advance_booking_days INT DEFAULT 30,
    cancellation_hours_before INT DEFAULT 24,
    no_show_penalty_percentage DECIMAL(5, 2) DEFAULT 10,
    peak_hours_start TIME,
    peak_hours_end TIME,
    peak_hours_multiplier DECIMAL(3, 2) DEFAULT 1.5,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **Bookings Table** (Core Transactions)
```sql
CREATE TABLE bookings (
    booking_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    court_id UUID REFERENCES courts(court_id),
    net_id UUID REFERENCES cricket_nets(net_id),
    table_id UUID REFERENCES ping_pong_tables(table_id),
    sport_id UUID NOT NULL REFERENCES sports(sport_id),
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    duration_minutes INT GENERATED ALWAYS AS (EXTRACT(EPOCH FROM (end_time - start_time))/60) STORED,
    number_of_players INT,
    booking_status ENUM('PENDING', 'CONFIRMED', 'CANCELLED', 'NO_SHOW', 'COMPLETED') DEFAULT 'PENDING',
    cancellation_reason TEXT,
    cancelled_by_user BOOLEAN,
    cancelled_at TIMESTAMP,
    notes TEXT,
    coach_id UUID REFERENCES users(user_id), -- Optional: booking with trainer
    skill_level VARCHAR(50), -- BEGINNER, INTERMEDIATE, ADVANCED
    is_recurring BOOLEAN DEFAULT FALSE,
    recurring_booking_id UUID, -- Reference to parent recurring booking
    recurring_end_date DATE, -- For recurring bookings
    lock_version INT DEFAULT 0, -- For optimistic locking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_time_slot CHECK (start_time < end_time)
);

CREATE INDEX idx_bookings_user ON bookings(user_id);
CREATE INDEX idx_bookings_court ON bookings(court_id);
CREATE INDEX idx_bookings_net ON bookings(net_id);
CREATE INDEX idx_bookings_table ON bookings(table_id);
CREATE INDEX idx_bookings_date_time ON bookings(booking_date, start_time, end_time);
CREATE INDEX idx_bookings_status ON bookings(booking_status);
CREATE INDEX idx_bookings_date_court ON bookings(booking_date, court_id) WHERE booking_status IN ('CONFIRMED', 'PENDING');
CREATE UNIQUE INDEX idx_court_timeslot ON bookings(court_id, booking_date, start_time, end_time) 
    WHERE booking_status IN ('CONFIRMED', 'PENDING');
```

#### **Equipment Inventory**
```sql
CREATE TABLE equipment_types (
    equipment_type_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    equipment_name VARCHAR(100) NOT NULL, -- 'Badminton Racquet', 'Pickleball Paddle', etc.
    description TEXT,
    sport_id UUID NOT NULL REFERENCES sports(sport_id),
    rental_price DECIMAL(10, 2),
    is_rental_available BOOLEAN DEFAULT TRUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE equipment_inventory (
    inventory_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    equipment_type_id UUID NOT NULL REFERENCES equipment_types(equipment_type_id),
    equipment_serial_number VARCHAR(100),
    purchase_date DATE,
    condition ENUM('EXCELLENT', 'GOOD', 'FAIR', 'NEEDS_REPAIR') DEFAULT 'EXCELLENT',
    status ENUM('AVAILABLE', 'RENTED', 'MAINTENANCE', 'RETIRED') DEFAULT 'AVAILABLE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE equipment_rentals (
    rental_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID NOT NULL REFERENCES bookings(booking_id),
    equipment_type_id UUID NOT NULL REFERENCES equipment_types(equipment_type_id),
    inventory_id UUID NOT NULL REFERENCES equipment_inventory(inventory_id),
    quantity INT NOT NULL DEFAULT 1,
    rental_price DECIMAL(10, 2),
    rental_status ENUM('PENDING', 'ISSUED', 'RETURNED', 'DAMAGED') DEFAULT 'PENDING',
    returned_at TIMESTAMP,
    damage_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_equipment_status ON equipment_inventory(status);
```

#### **Products (Retail)**
```sql
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100), -- 'Sports Gear', 'Safety Equipment', 'Accessories'
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    sku VARCHAR(100) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **Payments**
```sql
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(booking_id),
    user_id UUID NOT NULL REFERENCES users(user_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_type ENUM('FULL', 'PARTIAL', 'PAY_AT_VENUE') DEFAULT 'FULL',
    payment_method ENUM('STRIPE', 'PAYPAL', 'CASH', 'CARD') NOT NULL,
    transaction_id VARCHAR(255) UNIQUE,
    payment_status ENUM('PENDING', 'COMPLETED', 'FAILED', 'REFUNDED') DEFAULT 'PENDING',
    payment_date TIMESTAMP,
    refund_amount DECIMAL(10, 2),
    refund_reason TEXT,
    refund_date TIMESTAMP,
    receipt_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_payments_user ON payments(user_id);
CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_payments_status ON payments(payment_status);
```

#### **Waitlist**
```sql
CREATE TABLE waitlists (
    waitlist_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    court_id UUID REFERENCES courts(court_id),
    net_id UUID REFERENCES cricket_nets(net_id),
    table_id UUID REFERENCES ping_pong_tables(table_id),
    sport_id UUID NOT NULL REFERENCES sports(sport_id),
    desired_date DATE NOT NULL,
    desired_start_time TIME NOT NULL,
    desired_end_time TIME NOT NULL,
    position_in_queue INT,
    status ENUM('WAITING', 'NOTIFIED', 'EXPIRED', 'CANCELLED') DEFAULT 'WAITING',
    notification_sent BOOLEAN DEFAULT FALSE,
    notification_sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP DEFAULT (CURRENT_TIMESTAMP + INTERVAL '30 days')
);

CREATE INDEX idx_waitlist_user ON waitlists(user_id);
CREATE INDEX idx_waitlist_court ON waitlists(court_id);
CREATE INDEX idx_waitlist_status ON waitlists(status);
```

#### **Recurring Bookings**
```sql
CREATE TABLE recurring_bookings (
    recurring_booking_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    court_id UUID REFERENCES courts(court_id),
    net_id UUID REFERENCES cricket_nets(net_id),
    table_id UUID REFERENCES ping_pong_tables(table_id),
    sport_id UUID NOT NULL REFERENCES sports(sport_id),
    day_of_week INT NOT NULL, -- 0=Sunday, 6=Saturday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    recurrence_status ENUM('ACTIVE', 'PAUSED', 'CANCELLED') DEFAULT 'ACTIVE',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_recurring_user ON recurring_bookings(user_id);
CREATE INDEX idx_recurring_status ON recurring_bookings(recurrence_status);
```

#### **Notifications**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    booking_id UUID REFERENCES bookings(booking_id),
    notification_type ENUM('BOOKING_CONFIRMATION', 'REMINDER_24H', 'CANCELLATION', 'WAITLIST', 'PAYMENT_RECEIPT', 'ADMIN_ALERT') NOT NULL,
    channel ENUM('EMAIL', 'SMS', 'PUSH', 'IN_APP') NOT NULL,
    subject VARCHAR(255),
    message TEXT NOT NULL,
    recipient_address VARCHAR(255),
    status ENUM('PENDING', 'SENT', 'FAILED', 'DELIVERED') DEFAULT 'PENDING',
    retry_count INT DEFAULT 0,
    sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_status ON notifications(status);
```

#### **Incidents & Safety**
```sql
CREATE TABLE incidents (
    incident_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(booking_id),
    user_id UUID REFERENCES users(user_id),
    court_id UUID REFERENCES courts(court_id),
    incident_type VARCHAR(100), -- injury, property_damage, etc.
    description TEXT NOT NULL,
    severity ENUM('LOW', 'MEDIUM', 'HIGH', 'CRITICAL') DEFAULT 'MEDIUM',
    reported_by_user_id UUID NOT NULL REFERENCES users(user_id),
    status ENUM('REPORTED', 'UNDER_REVIEW', 'RESOLVED', 'CLOSED') DEFAULT 'REPORTED',
    resolution_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE safety_forms (
    form_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    form_type VARCHAR(100) NOT NULL, -- 'LIABILITY_RELEASE', 'SAFETY_WAIVER'
    signed_at TIMESTAMP NOT NULL,
    form_version VARCHAR(10) NOT NULL,
    pdf_url TEXT,
    signature_data JSON, -- Base64 or metadata about signature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_safety_forms_user ON safety_forms(user_id);
```

#### **Analytics & Audit**
```sql
CREATE TABLE booking_analytics (
    analytics_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    court_id UUID REFERENCES courts(court_id),
    booking_date DATE NOT NULL,
    total_bookings INT DEFAULT 0,
    completed_bookings INT DEFAULT 0,
    cancelled_bookings INT DEFAULT 0,
    no_show_count INT DEFAULT 0,
    total_revenue DECIMAL(12, 2) DEFAULT 0,
    peak_hours_utilization DECIMAL(5, 2),
    off_peak_hours_utilization DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(user_id),
    action VARCHAR(255) NOT NULL,
    resource_type VARCHAR(100),
    resource_id VARCHAR(100),
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_resource ON audit_logs(resource_type, resource_id);
```

### 2.2 Database Constraints & Relationships

```sql
-- Ensure only one resource type per booking
ALTER TABLE bookings ADD CONSTRAINT check_single_resource_per_booking
CHECK (
    (court_id IS NOT NULL AND net_id IS NULL AND table_id IS NULL) OR
    (court_id IS NULL AND net_id IS NOT NULL AND table_id IS NULL) OR
    (court_id IS NULL AND net_id IS NULL AND table_id IS NOT NULL)
);

-- Ensure waitlist has only one resource type
ALTER TABLE waitlists ADD CONSTRAINT check_single_resource_per_waitlist
CHECK (
    (court_id IS NOT NULL AND net_id IS NULL AND table_id IS NULL) OR
    (court_id IS NULL AND net_id IS NOT NULL AND table_id IS NULL) OR
    (court_id IS NULL AND net_id IS NULL AND table_id IS NOT NULL)
);
```

---

## 3. CLASS DIAGRAM (Object-Oriented Design)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        SYSTEM ARCHITECTURE CLASSES                       │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────┐
│      User (Abstract)     │
├──────────────────────────┤
│ - userId: UUID           │
│ - fullName: String       │
│ - email: String          │
│ - phone: String          │
│ - password: String       │
│ - userType: Enum         │
│ - status: Enum           │
│ - emergencyContact       │
│ - liabilityFormSigned    │
│ - createdAt: DateTime    │
├──────────────────────────┤
│ + login()                │
│ + updateProfile()        │
│ + viewBookingHistory()   │
│ + getContactInfo()       │
└──────────────────────────┘
         △    △    △
         │    │    └──────────────────────────┐
         │    │                               │
         │    └──────────────┐                │
         │                   │                │
    ┌────┴──────┐   ┌────────┴────┐  ┌──────┴──────┐
    │   Player   │   │    Coach    │  │    Admin    │
    ├────────────┤   ├─────────────┤  ├─────────────┤
    │ - stats    │   │ - specialty │  │ - permissions
    │ - rating   │   │ - availability
    └────────────┘   │ - schedule  │  └─────────────┘
                     └─────────────┘

┌──────────────────────────┐
│    SportResource         │
│     (Abstract)           │
├──────────────────────────┤
│ - resourceId: UUID       │
│ - resourceNumber: String │
│ - location: String       │
│ - capacity: Int          │
│ - hourlyRate: Decimal    │
│ - status: Enum           │
│ - sports: List<Sport>    │
├──────────────────────────┤
│ + isAvailable()          │
│ + getAvailableSlots()    │
│ + block()                │
│ + unblock()              │
│ + updateRate()           │
└──────────────────────────┘
         △    △    △
         │    │    │
    ┌────┴┐   │   ┌┴─────┐
    │     │   │   │      │
┌───┴──┐ ┌──┴──┐ ┌──┴───┐ ┌────┴────┐
│Court │ │Cricket  PingPong  (Future)
│      │ │ Net    │Table │ │Indoor Garden
└──────┘ └───────┘└──────┘ └──────────┘

┌──────────────────────────┐
│       Booking            │
├──────────────────────────┤
│ - bookingId: UUID        │
│ - userId: UUID           │
│ - resource: SportResource
│ - sport: Sport           │
│ - bookingDate: Date      │
│ - startTime: Time        │
│ - endTime: Time          │
│ - duration: Int          │
│ - status: Enum           │
│ - players: Int           │
│ - coach: User (optional) │
│ - notes: String          │
│ - isRecurring: Boolean   │
│ - lockedVersion: Int     │
├──────────────────────────┤
│ + createBooking()        │
│ + cancelBooking()        │
│ + rescheduleBooking()    │
│ + updateStatus()         │
│ + getPaymentInfo()       │
│ + addToWaitlist()        │
└──────────────────────────┘
         │
         │ 1..1
         ├─────────────┬────────────┬──────────────┐
         │             │            │              │
    ┌────┴────┐   ┌───┴────┐  ┌────┴───┐    ┌────┴────┐
    │ Payment  │   │Equipment  │Notification │Waitlist
    │          │   │ Rental     │             │
    └──────────┘   └────────────┘  ┌─────────────┐
                                  │ - position   │
                                  │ - status     │
                                  │ - expiresAt  │
                                  └──────────────┘

┌──────────────────────────┐
│       Payment            │
├──────────────────────────┤
│ - paymentId: UUID        │
│ - bookingId: UUID        │
│ - userId: UUID           │
│ - amount: Decimal        │
│ - type: Enum             │
│ - method: Enum           │
│ - transactionId: String  │
│ - status: Enum           │
│ - paymentDate: DateTime  │
│ - receipt: String (URL)  │
├──────────────────────────┤
│ + processPayment()       │
│ + refund()               │
│ + generateReceipt()      │
│ + validatePayment()      │
└──────────────────────────┘

┌──────────────────────────┐
│    Notification          │
├──────────────────────────┤
│ - notificationId: UUID   │
│ - userId: UUID           │
│ - type: Enum             │
│ - channel: Enum          │
│ - subject: String        │
│ - message: String        │
│ - status: Enum           │
│ - sentAt: DateTime       │
├──────────────────────────┤
│ + send()                 │
│ + retry()                │
│ + markAsSent()           │
└──────────────────────────┘

┌──────────────────────────┐
│      Equipment           │
├──────────────────────────┤
│ - equipmentId: UUID      │
│ - typeId: UUID           │
│ - serialNumber: String   │
│ - purchaseDate: Date     │
│ - condition: Enum        │
│ - status: Enum           │
├──────────────────────────┤
│ + checkOut()             │
│ + checkIn()              │
│ + markForRepair()        │
│ + retire()               │
└──────────────────────────┘

┌──────────────────────────┐
│       Analytics          │
├──────────────────────────┤
│ - analyticsId: UUID      │
│ - resourceId: UUID       │
│ - date: Date             │
│ - totalBookings: Int     │
│ - revenue: Decimal       │
│ - utilization: Decimal   │
├──────────────────────────┤
│ + generateReport()       │
│ + calculateMetrics()     │
│ + getPeakHours()         │
│ + getUtilizationRate()   │
└──────────────────────────┘

┌──────────────────────────┐
│       SafetyForm         │
├──────────────────────────┤
│ - formId: UUID           │
│ - userId: UUID           │
│ - formType: String       │
│ - signedAt: DateTime     │
│ - version: String        │
│ - pdfUrl: String         │
├──────────────────────────┤
│ + sign()                 │
│ + verify()               │
│ + getPdfCopy()           │
│ + expire()               │
└──────────────────────────┘

┌──────────────────────────┐
│      Incident            │
├──────────────────────────┤
│ - incidentId: UUID       │
│ - bookingId: UUID        │
│ - type: String           │
│ - severity: Enum         │
│ - description: String    │
│ - status: Enum           │
├──────────────────────────┤
│ + reportIncident()       │
│ + updateStatus()         │
│ + resolve()              │
│ + attachDocuments()      │
└──────────────────────────┘
```

---

## 4. SYSTEM DESIGN - HIGH LEVEL ARCHITECTURE (HLD)

```
┌───────────────────────────────────────────────────────────────────────────┐
│                   SPORTS ACADEMY BOOKING SYSTEM - HLD                      │
└───────────────────────────────────────────────────────────────────────────┘

                              CLIENT LAYER
    ┌─────────────────────────────────────────────────────────────┐
    │  Web Application (React)  │  Mobile App (React Native)     │
    │  Admin Dashboard          │  Player App                    │
    │  Coach Portal             │  Coach App                     │
    └──────────────┬────────────────────────────┬────────────────┘
                   │                            │
                   └────────────────┬───────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │  API GATEWAY (Kong/AWS)       │
                    │ - Rate Limiting               │
                    │ - Request Validation          │
                    │ - Authentication              │
                    │ - Load Balancing              │
                    └───────────┬────────────────────┘
                                │
              APPLICATION LAYER
    ┌───────────────────────────▼──────────────────────────────────┐
    │                                                               │
    │  ┌──────────────────┐  ┌──────────────────┐  ┌────────────┐ │
    │  │  User Service    │  │ Booking Service  │  │ Notification
    │  │  - Register      │  │ - Create Booking │  │ Service    │
    │  │  - Login         │  │ - Cancel Booking │  │ - Email    │
    │  │  - Profile Mgmt  │  │ - Check Conflict │  │ - SMS      │
    │  │  - Form Signing  │  │ - Reserve Slot   │  │ - Push     │
    │  │                  │  │ - Sync Calendar  │  │            │
    │  └──────────────────┘  └──────────────────┘  └────────────┘
    │  ┌──────────────────┐  ┌──────────────────┐  ┌────────────┐ │
    │  │ Court Service    │  │ Payment Service  │  │ Equipment  │
    │  │ - Availability   │  │ - Process Payment│  │ Service    │
    │  │ - Block/Unblock  │  │ - Refund         │  │ - Inventory│
    │  │ - Get Slots      │  │ - Receipt        │  │ - Rental   │
    │  │ - Ping Pong Logic│  │ - Stripe/PayPal  │  │ - Tracking │
    │  │ - Cricket Logic  │  │ Integration      │  │            │
    │  └──────────────────┘  └──────────────────┘  └────────────┘
    │  ┌──────────────────┐  ┌──────────────────┐  ┌────────────┐ │
    │  │ Analytics Service│  │ Waitlist Service │  │ Admin      │
    │  │ - Reports        │  │ - Queue Mgmt     │  │ Service    │
    │  │ - Utilization    │  │ - Notifications  │  │ - Dashboard│
    │  │ - Revenue        │  │ - Auto-Notify    │  │ - Reports  │
    │  │ - Peak Hours     │  │ - Expiry Mgmt    │  │ - Settings │
    │  └──────────────────┘  └──────────────────┘  └────────────┘
    │                                                               │
    └────────────┬──────────────────────────────┬─────────────────┘
                 │                              │
        SHARED UTILITIES & LIBRARIES
    ┌────────────▼──────────────────────────────▼─────────────────┐
    │ - Authentication (JWT/OAuth2)                               │
    │ - Authorization (RBAC)                                      │
    │ - Error Handling                                            │
    │ - Logging & Monitoring                                      │
    │ - Caching Layer (Redis)                                     │
    │ - Message Queue (RabbitMQ)                                  │
    └────────────┬──────────────────────────────┬─────────────────┘
                 │                              │
                 DATA ACCESS LAYER
    ┌────────────▼──────────────────────────────▼─────────────────┐
    │  ┌──────────────────────────────────────────────────────┐   │
    │  │  ORM Layer (JPA/Hibernate or Sequelize)              │   │
    │  │  Repository Pattern                                  │   │
    │  │  Query Optimization                                  │   │
    │  │  Connection Pooling                                  │   │
    │  └────────────┬────────────────────────────────┬────────┘   │
    │               │                                │              │
    │  ┌────────────▼────────────┐  ┌───────────────▼────────┐    │
    │  │  Primary Database       │  │  Read Replica           │    │
    │  │  (PostgreSQL)           │  │  (PostgreSQL Replica)   │    │
    │  │  - Write Operations     │  │  - Read Operations      │    │
    │  │  - Transactions         │  │  - Analytics Queries    │    │
    │  │  - ACID Compliance      │  │  - Reports              │    │
    │  └────────────┬────────────┘  └───────────────┬────────┘    │
    │               │                                │              │
    │  ┌────────────▼────────────────────────────────▼────────┐    │
    │  │  Backup & Recovery                                   │    │
    │  │  - Daily Backups                                     │    │
    │  │  - Point-in-Time Recovery                            │    │
    │  │  - Disaster Recovery Plan                            │    │
    │  └──────────────────────────────────────────────────────┘    │
    └────────────┬───────────────────────────────┬─────────────────┘
                 │                               │
        EXTERNAL INTEGRATIONS
    ┌────────────▼───────────────────────────────▼─────────────────┐
    │  ┌──────────────────┐  ┌───────────────┐  ┌───────────────┐  │
    │  │  Payment Gateway │  │ Email Service │  │ SMS Gateway   │  │
    │  │  - Stripe        │  │ - SendGrid    │  │ - Twilio      │  │
    │  │  - PayPal        │  │ - AWS SES     │  │ - AWS SNS     │  │
    │  └──────────────────┘  └───────────────┘  └───────────────┘  │
    │  ┌──────────────────┐  ┌───────────────┐  ┌───────────────┐  │
    │  │  Cloud Storage   │  │ File Service  │  │ Calendar API  │  │
    │  │  - AWS S3        │  │ - PDF Gen     │  │ - Google Cal  │  │
    │  │  - Backup Store  │  │ - Document    │  │ - Outlook API │  │
    │  └──────────────────┘  └───────────────┘  └───────────────┘  │
    └────────────┬───────────────────────────────┬─────────────────┘
                 │                               │
        INFRASTRUCTURE & DEVOPS
    ┌────────────▼───────────────────────────────▼─────────────────┐
    │  ┌──────────────────────────────────────────────────────┐    │
    │  │  Containerization (Docker)                           │    │
    │  │  Orchestration (Kubernetes)                          │    │
    │  │  Service Mesh (Istio)                                │    │
    │  │  Load Balancer (Nginx/HAProxy)                       │    │
    │  └──────────────────────────────────────────────────────┘    │
    │  ┌──────────────────────────────────────────────────────┐    │
    │  │  Monitoring & Logging                                │    │
    │  │  - ELK Stack (Elasticsearch, Logstash, Kibana)       │    │
    │  │  - Prometheus + Grafana                              │    │
    │  │  - DataDog / New Relic                               │    │
    │  └──────────────────────────────────────────────────────┘    │
    │  ┌──────────────────────────────────────────────────────┐    │
    │  │  CI/CD Pipeline                                      │    │
    │  │  - GitHub/GitLab Actions                             │    │
    │  │  - Jenkins                                           │    │
    │  │  - Automated Testing                                 │    │
    │  │  - Blue-Green Deployments                            │    │
    │  └──────────────────────────────────────────────────────┘    │
    └────────────────────────────────────────────────────────────────┘
```

### 4.1 Data Flow Diagrams

#### **Booking Creation Flow**
```
┌─────────┐
│ Player  │
└────┬────┘
     │ 1. Browse Available Slots
     ▼
┌──────────────────────────┐
│ Availability Check       │
│ - Get court slots        │
│ - Apply filters          │
│ - Check capacity         │
└────┬─────────────────────┘
     │ 2. Fetch Available Slots
     ▼
┌──────────────────────────┐
│ Booking Service          │
│ - Verify timeslot free   │
│ - Check rules (ping pong)│
│ - Calculate rate         │
│ - Check user eligibility │
└────┬─────────────────────┘
     │ 3. Submit Booking Request
     ▼
┌──────────────────────────┐         ┌──────────────────┐
│ Optimistic Lock Check    │◄────────│ Database Lock    │
│ - Current version        │         │ Version Control  │
│ - Prevent concurrent     │         └──────────────────┘
│   double bookings        │
└────┬─────────────────────┘
     │ 4. Lock & Insert
     ▼
┌──────────────────────────┐
│ Database Transaction     │
│ - Insert Booking         │
│ - Update Court Status    │
│ - Create Payment Record  │
│ - Commit                 │
└────┬─────────────────────┘
     │ 5. Booking Confirmed
     ▼
┌──────────────────────────┐
│ Payment Processing       │
│ - Stripe/PayPal          │
│ - Update Payment Status  │
└────┬─────────────────────┘
     │ 6. Payment Success
     ▼
┌──────────────────────────┐
│ Notification System      │
│ - Email Confirmation     │
│ - SMS Reminder           │
│ - Push Notification      │
└────┬─────────────────────┘
     │
     ▼
┌─────────┐
│ Player  │ (Receives Confirmation)
└─────────┘
```

#### **Real-Time Sync Flow**
```
┌─────────────────────────────────────────────────────────────┐
│           WebSocket Connection (Player Sessions)            │
└─────────────┬───────────────────────────┬───────────────────┘
              │                           │
        ┌─────▼────┐              ┌──────▼────┐
        │ Player A │              │ Player B  │
        └─────┬────┘              └──────┬────┘
              │                          │
              │ Subscribe to Court      │ Subscribe to Court
              │ Availability Updates    │ Availability Updates
              │                         │
        ┌─────▼─────────────────────────▼────┐
        │  Redis Channel (court:id:updates)  │
        │  - Booking state changes           │
        │  - Real-time sync                  │
        │  - Lock acquisitions               │
        └─────┬──────────────────────────────┘
              │
        ┌─────▼──────────────────┐
        │ Booking Service        │
        │ - Detects conflict     │
        │ - Publishes to channel │
        │ - Updates Redis state  │
        └─────┬──────────────────┘
              │
        ┌─────▼──────────────────┐
        │ Database (PostgreSQL)  │
        │ - Persists changes     │
        └────────────────────────┘
```

---

## 5. TECHNOLOGY STACK RECOMMENDATION

### 5.1 Backend Technology Stack

| Layer | Technology | Justification |
|-------|-----------|--------------|
| **Language** | Java 17+ / Python 3.10+ | Enterprise-grade, scalable, large ecosystem |
| **Framework** | Spring Boot 3.x (Java) / FastAPI (Python) | Mature, production-ready, strong community |
| **API** | REST + GraphQL | REST for primary APIs, GraphQL for flexible queries |
| **Async Processing** | Spring WebFlux / Async/Await | Handle concurrent requests efficiently |
| **Real-Time** | WebSockets (Socket.io / Spring WebSocket) | Live booking updates, sync |
| **Caching** | Redis 7.x | Session storage, real-time locks, rate limiting |
| **Message Queue** | RabbitMQ / Apache Kafka | Async notifications, scheduled tasks |
| **ORM** | Hibernate 6.x / SQLAlchemy | Type-safe database access |
| **Validation** | Bean Validation (Hibernate Validator) | Input validation framework |
| **Testing** | JUnit 5, Mockito, TestContainers | Unit, integration, contract testing |
| **Security** | Spring Security 6.x, OAuth2, JWT | Authentication, authorization, encryption |
| **Logging** | Slf4j + Logback / Python logging | Structured logging, log aggregation ready |

### 5.2 Frontend Technology Stack

| Layer | Technology | Justification |
|-------|-----------|--------------|
| **Web Framework** | React 18+ | Component-based, SEO, large ecosystem |
| **Mobile Framework** | React Native / Flutter | Cross-platform, code reuse |
| **State Management** | Redux Toolkit / Zustand | Centralized state, time-travel debugging |
| **HTTP Client** | Axios / React Query | Data fetching, caching, synchronization |
| **Real-Time** | Socket.io-client / WebSocket API | Live updates, push notifications |
| **UI Library** | Material-UI (MUI) / Chakra UI | Rich components, accessibility |
| **Styling** | TailwindCSS / Styled Components | Utility-first CSS |
| **Forms** | React Hook Form | Lightweight, performant form handling |
| **Validation** | Zod / Yup | Runtime type checking |
| **Date/Time** | Day.js / date-fns | Lightweight date manipulation |
| **Calendar** | React-Big-Calendar / FullCalendar | Interactive calendar widget |
| **Payment UI** | Stripe.js / PayPal SDK | Secure payment collection |
| **Testing** | Vitest, Testing Library, Cypress | Unit, component, E2E testing |
| **Build** | Vite | Fast bundling, HMR |

### 5.3 Database Stack

| Component | Technology | Justification |
|-----------|-----------|--------------|
| **Primary DB** | PostgreSQL 15+ | ACID compliance, JSON support, advanced indexing |
| **Read Replica** | PostgreSQL Replica | Analytics queries, reporting |
| **Cache** | Redis 7.x | Session, locks, real-time data |
| **Search** | Elasticsearch 8.x | Full-text search (future), analytics |
| **Analytics** | TimescaleDB / ClickHouse | Time-series data, analytics queries |
| **Backup** | AWS S3 / MinIO | Off-site backups, disaster recovery |

### 5.4 Infrastructure & DevOps

| Component | Technology | Justification |
|-----------|-----------|--------------|
| **Containerization** | Docker 24.x | Consistency, portability |
| **Orchestration** | Kubernetes 1.28+ | Auto-scaling, self-healing, service mesh |
| **Service Mesh** | Istio / Linkerd | Traffic management, security policies |
| **API Gateway** | Kong / AWS API Gateway | Rate limiting, authentication, load balancing |
| **Load Balancer** | Nginx / HAProxy | High availability, SSL termination |
| **Cloud Platform** | AWS / GCP / Azure | Managed services, scalability |
| **CI/CD** | GitHub Actions / GitLab CI / Jenkins | Automated testing, deployment |
| **Monitoring** | Prometheus + Grafana | Metrics, alerting, dashboards |
| **Logging** | ELK Stack (Elasticsearch, Logstash, Kibana) | Centralized logging, analysis |
| **Tracing** | Jaeger / Zipkin | Distributed tracing, performance analysis |
| **Container Registry** | Docker Hub / AWS ECR | Image storage, versioning |
| **Secrets Management** | HashiCorp Vault / AWS Secrets Manager | Secure credential storage |
| **Configuration Mgmt** | Spring Cloud Config / Consul | Centralized configuration |

### 5.5 Third-Party Integrations

| Service | Provider | Purpose |
|---------|----------|---------|
| **Payment Gateway** | Stripe / PayPal | Payment processing |
| **Email Service** | SendGrid / AWS SES / Mailgun | Transactional emails |
| **SMS Gateway** | Twilio / AWS SNS | SMS notifications |
| **Push Notifications** | Firebase Cloud Messaging / OneSignal | Mobile push alerts |
| **File Storage** | AWS S3 / Google Cloud Storage | PDF storage, documents |
| **Document Generation** | iText / Apache PDFBox | PDF receipt/form generation |
| **Calendar API** | Google Calendar / Microsoft Graph | Calendar integration |
| **Analytics** | Google Analytics / Mixpanel | User behavior tracking |

---

## 6. PROPOSED TECH STACK CONFIGURATION

### 6.1 Recommended Stack (Production-Ready)

```
┌──────────────────────────────────────────────────────────────┐
│                   RECOMMENDED TECH STACK                      │
├──────────────────────────────────────────────────────────────┤
│ BACKEND:                                                      │
│ ├─ Language: Java 17 + Spring Boot 3.2                       │
│ ├─ Database: PostgreSQL 15 (Primary + Read Replica)          │
│ ├─ Cache: Redis 7                                            │
│ ├─ Message Queue: RabbitMQ 3.12                              │
│ ├─ Real-Time: Spring WebSocket + Redis Streams              │
│ ├─ Search: Elasticsearch 8.10 (optional, future)             │
│ └─ API: REST (HAL) + GraphQL (Apollo)                        │
│                                                               │
│ FRONTEND:                                                     │
│ ├─ Web: React 18 + TypeScript 5                              │
│ ├─ Mobile: React Native / Flutter                            │
│ ├─ State: Redux Toolkit                                      │
│ ├─ Forms: React Hook Form                                    │
│ ├─ Calendar: FullCalendar v6                                 │
│ └─ Styling: TailwindCSS + Radix UI                           │
│                                                               │
│ INFRASTRUCTURE:                                               │
│ ├─ Container: Docker 24                                      │
│ ├─ Orchestration: Kubernetes 1.28                            │
│ ├─ Cloud: AWS (ECS/EKS, RDS, S3, ElastiCache)               │
│ ├─ CI/CD: GitHub Actions / GitLab CI                         │
│ ├─ Monitoring: Prometheus + Grafana + ELK                    │
│ └─ IaC: Terraform / CloudFormation                           │
│                                                               │
│ INTEGRATIONS:                                                 │
│ ├─ Payment: Stripe (primary) + PayPal                        │
│ ├─ Email: SendGrid                                           │
│ ├─ SMS: Twilio                                               │
│ └─ Push: Firebase Cloud Messaging                            │
└──────────────────────────────────────────────────────────────┘
```

### 6.2 Alternative Stack (Lean/Startup)

```
For faster MVP with reduced complexity:
- Backend: Node.js + Express.js / Python + FastAPI
- Database: PostgreSQL + Redis
- Frontend: Next.js (SSR benefits)
- Mobile: Flutter
- Cloud: AWS Amplify / Firebase
- CI/CD: GitHub Actions
```

---

## 7. KEY ARCHITECTURAL DECISIONS

### 7.1 Concurrency Control Strategy

**Problem:** Prevent double bookings when multiple users book simultaneously.

**Solution:** Optimistic Locking + Pessimistic Lock Backup
```
1. Optimistic Locking (default):
   - Each booking has lock_version field
   - On update, check version hasn't changed
   - Retry if conflict (version mismatch)
   - Minimizes lock contention

2. Pessimistic Lock (fallback):
   - Use Redis distributed lock
   - Key: "lock:court:{courtId}:{date}:{startTime}"
   - TTL: 5 seconds (max operation time)
   - Fallback if optimistic fails

3. Database Unique Index:
   - Unique constraint on (court_id, booking_date, start_time, end_time)
   - Prevents physical duplicate inserts
   - Final safety net
```

### 7.2 Complex Business Logic (Ping Pong & Cricket)

**Implemented as Service Layer:**
```java
public class CourtAvailabilityService {
    // Ping Pong Logic:
    // 2 ping pong tables → 1 indoor court blocked
    // Cricket Nets: 3 nets, affects indoor courts
    
    public List<TimeSlot> getAvailableSlots(CourtRequest request) {
        if (request.isCricket()) {
            return cricketNetAvailability(request);
        } else if (request.isPingPong()) {
            return pingPongTableLogic(request);
        } else {
            return standardCourtAvailability(request);
        }
    }
    
    private List<TimeSlot> pingPongTableLogic(CourtRequest request) {
        // If ≥2 ping pong tables booked → block 1 indoor court
        // Otherwise → all 3 indoor courts available for badminton/pickleball
    }
    
    private List<TimeSlot> cricketNetAvailability(CourtRequest request) {
        // Cricket net booking affects indoor court availability
        // Manage 3 nets with dependencies
    }
}
```

### 7.3 Notification Strategy

**Asynchronous Event-Driven:**
```
1. Booking Event Published → RabbitMQ
2. Notification Service Consumes → Generates notifications
3. Multi-channel delivery (Email, SMS, Push)
4. Retry mechanism with exponential backoff
5. Fallback graceful degradation
```

### 7.4 Caching Strategy

```
Redis Cache Layers:
- User sessions (TTL: 24 hours)
- Available court slots (TTL: 5 minutes, invalidate on booking)
- Equipment inventory (TTL: 10 minutes)
- Admin dashboards (TTL: 1 hour)
- Frequently accessed analytics (TTL: 6 hours)
```

---

## 8. SECURITY CONSIDERATIONS

### 8.1 Authentication & Authorization

- **OAuth2 + JWT** for API endpoints
- **Role-Based Access Control (RBAC)**: Player, Coach, Admin, SuperAdmin
- **MFA (Multi-Factor Authentication)** for admin accounts
- **Session timeout**: 30 minutes
- **Password policy**: Minimum 12 characters, complexity rules

### 8.2 Data Protection

- **Encryption at Rest**: AES-256 (database, backups)
- **Encryption in Transit**: TLS 1.3
- **PII Encryption**: SSN, payment info
- **Data Masking**: Audit logs, support access
- **GDPR Compliance**: Right to be forgotten, data export

### 8.3 Payment Security

- **PCI-DSS Compliance**: Never store raw card data
- **Tokenization**: Stripe/PayPal tokens only
- **3D Secure**: For high-value transactions
- **Fraud Detection**: Monitor suspicious patterns

### 8.4 API Security

- **Rate Limiting**: 100 req/min per user
- **Input Validation**: Whitelist allowed characters
- **SQL Injection Prevention**: Parameterized queries (ORM)
- **CSRF Protection**: Token validation
- **CORS**: Whitelist frontend domains
- **API Versioning**: v1/, v2/ endpoints

---

## 9. SCALABILITY & PERFORMANCE

### 9.1 Scalability Measures

| Concern | Solution |
|---------|----------|
| **Horizontal Scaling** | Stateless services, load balancer, Kubernetes |
| **Database Scaling** | Read replicas, sharding (future), connection pooling |
| **Caching** | Redis cluster, cache-aside pattern |
| **Asynchronous Tasks** | Message queue, background workers |
| **CDN** | CloudFront for static assets |

### 9.2 Performance Targets

- **API Response Time**: <200ms (p95)
- **Page Load Time**: <2s (web)
- **Database Query**: <100ms (p95)
- **Throughput**: 1000 req/sec
- **Concurrent Users**: 10,000
- **Real-Time Sync**: <500ms latency

### 9.3 Caching Strategy

```
┌─────────┐
│ Request │
└────┬────┘
     │ Check Redis Cache
     ▼
┌──────────────────┐ HIT   ┌────────┐
│ Redis Cluster    ├──────→│ Client │
└────────┬─────────┘       └────────┘
         │ MISS
         ▼
┌──────────────────┐
│ PostgreSQL       │
│ (with caching)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Store in Redis   │
│ TTL: Context-    │
│ dependent        │
└────────┬─────────┘
         │
         ▼
     ┌────────┐
     │ Client │
     └────────┘

Cache Invalidation Strategy:
- Time-based (TTL)
- Event-based (booking changes)
- Manual (admin purge)
- Dependency-based (cascade invalidation)
```

---

## 10. IMPLEMENTATION ROADMAP

### Phase 1 (MVP - 3 months)
- [ ] Core booking system
- [ ] Basic court management
- [ ] Simple payment integration (Stripe)
- [ ] Email notifications
- [ ] Basic admin dashboard
- [ ] Single sport focus (Badminton)

### Phase 2 (6 months)
- [ ] Multi-sport support (Cricket, Pickleball, Ping Pong)
- [ ] Equipment rental system
- [ ] SMS notifications
- [ ] Waitlist functionality
- [ ] Recurring bookings
- [ ] Mobile app MVP

### Phase 3 (9 months)
- [ ] Advanced analytics & reporting
- [ ] Push notifications
- [ ] Coach/trainer booking
- [ ] Membership plans
- [ ] Dynamic pricing
- [ ] Incident logging system

### Phase 4 (12 months)
- [ ] Payment gateway options (PayPal, etc.)
- [ ] Google Calendar integration
- [ ] Social sharing features
- [ ] AI-powered recommendations
- [ ] Capacity optimization algorithm
- [ ] Full mobile app launch

---

## 11. RISK MITIGATION

| Risk | Mitigation |
|------|-----------|
| **Double Bookings** | Optimistic locking + unique index + Redis locks |
| **Payment Failures** | Stripe webhooks, retry logic, transaction logs |
| **Data Loss** | Daily backups, point-in-time recovery, replication |
| **Downtime** | Multi-region deployment, failover, auto-scaling |
| **Unauthorized Access** | OAuth2, JWT, RBAC, audit logs, IP whitelisting |
| **Notification Failures** | Queue retry, multiple channels, fallback emails |
| **Race Conditions** | Distributed locks, transactional consistency |

---

## 12. MONITORING & OBSERVABILITY

### 12.1 Key Metrics to Monitor

```
Performance Metrics:
- API response times (p50, p95, p99)
- Database query times
- Cache hit ratio
- Request throughput
- Error rates by endpoint

Business Metrics:
- Bookings per day
- Revenue per day
- Customer acquisition cost (CAC)
- Customer lifetime value (CLV)
- Court utilization rate
- Peak hour patterns

System Metrics:
- CPU, memory, disk usage
- Network latency
- Service availability (uptime %)
- Deployment frequency
- Lead time for changes
```

### 12.2 Alert Thresholds

```
Critical:
- API error rate > 1% → Page on-call
- Database down → Immediate escalation
- Payment gateway unavailable → Alert finance
- Booking queue depth > 1000 → Scale up

Warning:
- Response time p95 > 500ms → Investigate
- Cache hit ratio < 60% → Review TTLs
- Disk usage > 80% → Provision capacity
```

---

## 13. DEPLOYMENT ARCHITECTURE

```
┌────────────────────────────────────────────────────────────┐
│           Multi-Environment Deployment                      │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  Development (Local)                                        │
│  ├─ Docker Compose                                          │
│  ├─ PostgreSQL (local)                                      │
│  ├─ Redis (local)                                           │
│  └─ Stripe/PayPal Sandbox                                   │
│                                                             │
│  Staging (AWS)                                              │
│  ├─ ECS Fargate Cluster                                     │
│  ├─ RDS PostgreSQL                                          │
│  ├─ ElastiCache (Redis)                                     │
│  ├─ Test Data                                               │
│  └─ Staging Stripe Account                                  │
│                                                             │
│  Production (Multi-Region)                                  │
│  ├─ EKS Kubernetes Cluster                                  │
│  ├─ Multi-AZ RDS (Primary + Standby)                        │
│  ├─ Read Replica for Analytics                              │
│  ├─ ElastiCache (Redis Cluster)                             │
│  ├─ CloudFront CDN                                          │
│  ├─ Route 53 (DNS)                                          │
│  ├─ Production Stripe Account                               │
│  └─ Auto-scaling (2-20 replicas)                            │
│                                                             │
│  Blue-Green Deployment Strategy                            │
│  ├─ Two identical production environments                   │
│  ├─ Zero-downtime deployments                               │
│  ├─ Instant rollback capability                             │
│  └─ A/B testing support                                     │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## 14. COST ESTIMATION (Annual - AWS)

| Component | Monthly | Annual | Notes |
|-----------|---------|--------|-------|
| **EKS Cluster** | $150 | $1,800 | Management fee |
| **EC2 Instances** | $800 | $9,600 | 4-8 nodes, auto-scaling |
| **RDS PostgreSQL** | $500 | $6,000 | Multi-AZ, backups |
| **ElastiCache Redis** | $200 | $2,400 | Cluster mode |
| **S3 Storage** | $100 | $1,200 | Document storage, backups |
| **CloudFront** | $200 | $2,400 | CDN for static assets |
| **Data Transfer** | $100 | $1,200 | Outbound traffic |
| **RabbitMQ Managed** | $200 | $2,400 | Message queuing |
| **Monitoring (DataDog)** | $500 | $6,000 | APM, logs, metrics |
| **Backups & DR** | $150 | $1,800 | Cross-region backups |
| **Miscellaneous** | $200 | $2,400 | Domain, SSL, etc. |
| **TOTAL** | **$3,700** | **$44,800** | Conservative estimate |

*Note: Costs scale with user base. First 1 year development infrastructure cost not included.*

---

## CONCLUSION

This architecture provides a **scalable, secure, and maintainable** solution for the Sports Academy Court Booking System. The recommended tech stack balances maturity, community support, and production readiness. Implementation should follow the phased roadmap, with careful attention to concurrency control for double-booking prevention and real-time synchronization.

**Key Deliverables:**
✅ Comprehensive database design with proper normalization
✅ Object-oriented class diagram with service patterns
✅ Detailed HLD with all layers and interactions
✅ Production-ready tech stack recommendations
✅ Risk mitigation and security measures
✅ Scalability and performance considerations
