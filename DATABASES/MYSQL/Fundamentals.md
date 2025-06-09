## 📌 What is Data?
> Data is raw facts, figures, or statistics collected for reference or analysis. It has no meaning until it is processed.

Types of Data:
- Structured Data: Organized into rows & columns (e.g., tables in a database).
- Unstructured Data: No fixed format (e.g., emails, images, videos).
- Semi-Structured Data: Partially organized (e.g., XML, JSON).
- Metadata: Data about data (e.g., file size, creation date).


## 📌 What is a Database?
> A database is a structured collection of data that can be easily accessed, managed, and updated.

Key Characteristics:
- Stores data in a systematic way.
- Supports efficient retrieval, insertion, and modification.
- Maintains data integrity and security.

<img src="https://images.squarespace-cdn.com/content/v1/5f40c09c48e0fd517ae1f97b/1598788724225-1LNGVD6GP7XYMUDQV9G8/Database.jpg" width="600">

--

## 📌 Evolution of Databases
1. `Flat File Systems (1950s–60s)`:
- Data stored in plain text files.
- No relationships between data.

2. `Hierarchical Databases (e.g., IBM IMS)`:
- Tree-like structure.
- Rigid parent-child relationships.

3. `Network Databases (e.g., CODASYL)`:
- More flexible than hierarchical.
- Complex relationships allowed.

4. `Relational Databases (RDBMS) (1970s–)`:
- Tables with rows & columns.
- Based on SQL.
- Example: MySQL, PostgreSQL, Oracle.

5. `NoSQL Databases (2000s–`):`
- For big data, unstructured data.
- Example: MongoDB, Cassandra.

6. `NewSQL (2010s–)`:
- Combines benefits of SQL and scalability of NoSQL.
- Example: CockroachDB, Google Spanner.

## 📌 Types of Databases
* Relational Databases (RDBMS): MySQL, PostgreSQL
* NoSQL Databases: MongoDB, Cassandra, Redis
* In-Memory Databases: Redis, Memcached
* Time-Series Databases: InfluxDB, TimescaleDB
* Graph Databases: Neo4j, ArangoDB
* Object-Oriented Databases: db4o, ObjectDB
* Cloud Databases: Amazon RDS, Firebase, Google BigQuery
* Distributed Databases: Apache Cassandra, CockroachDB


## 📌 What is a DBMS (Database Management System)?
> Software that interacts with end users and databases to manage data.
- Functions of DBMS:
    - Data storage, retrieval, and update
    - Concurrency control
    - Backup & recovery
    - Security management
    - Data integrity

- Examples: MySQL, PostgreSQL, Oracle DB, SQL Server

<img src="https://www.quest.com/images/og/DBMS-OGImage_166634.jpg" width="600">

---
## 📌 What is MySQL?

> MySQL is an open-source relational database management system based on SQL (Structured Query Language). It's known for its speed, reliability, and ease of use.

Key Features:
- ACID compliant (with InnoDB)
- Supports joins, transactions, stored procedures
- Works well in web applications (LAMP stack)
- MySQL is free and open-source.
- MySQL is the DBMS behind some of the top websites and web-based applications in the world, including Airbnb, Uber, LinkedIn, Facebook, Twitter, and YouTube.
- MySQL is ideal for both small and large applications.

## ⚙️ How MySQL Works Internally

**1.Client Layer**
- User sends a query using a MySQL client or API.
- Query is passed to the MySQL server via TCP/IP.

**2. Parser & Optimizer**
- **Parser** checks SQL syntax.
- **Optimizer** decides the best query execution plan (e.g., index use, join order).

**3. Query Execution Engine**
- Executes the parsed and optimized query.

**4. Storage Engine Layer**
- Handles the actual data read/write operations.
- MySQL supports multiple storage engines:
  - **InnoDB (default):** Transaction-safe, row-level locking.
  - **MyISAM:** Fast reads, but no transaction support.
  - **Others:** MEMORY, CSV, ARCHIVE.

**5. Data Storage**
- Tables are stored as files.
- InnoDB stores data in:
  - Tablespaces
  - Redo logs
  - Undo logs (for transactions)

**6. Buffer Pool**
- Caches frequently accessed data in memory to improve performance.

**7. Redo Logs & Binary Logs**
- **Redo logs:** Ensure recovery in case of crash scenarios.
- **Binary logs:** Used for replication and backup.

<img src="https://dev.mysql.com/doc/refman/8.0/en/images/mysql-architecture.png" width="600">

---

## 📁 Relational vs Non-Relational Databases
| Aspect                 | **Relational (RDBMS)**                    | **Non-Relational (NoSQL)**                         |
| ---------------------- | ----------------------------------------- | -------------------------------------------------- |
| **Structure**          | Uses relations (tables)                   | Uses different formats (document, key-value, etc.) |
| **Data Integrity**     | Enforced via foreign keys, constraints    | Application-level logic handles integrity          |
| **Flexibility**        | Rigid – schema must be defined in advance | Flexible – can store varied and nested data        |
| **Normalization**      | Highly normalized to reduce redundancy    | Denormalization is common for performance          |
| **Storage Format**     | Row-based                                 | Varies (JSON, BSON, key-value pairs)               |
| **Data Relationships** | Strong and enforced via joins             | Weak or application-handled                        |



## 📊 SQL vs NoSQL
| Feature                 | **SQL** (Relational)                  | **NoSQL** (Non-Relational)                         |
| ----------------------- | ------------------------------------- | -------------------------------------------------- |
| **Full Form**           | Structured Query Language             | Not Only SQL                                       |
| **Data Model**          | Tables with rows and columns          | Document, Key-Value, Graph, or Column-Family       |
| **Schema**              | Fixed, predefined schema              | Flexible, dynamic schema                           |
| **Query Language**      | SQL                                   | Varies (JSON queries, API calls, etc.)             |
| **Scalability**         | Vertical (scale-up)                   | Horizontal (scale-out)                             |
| **Transactions (ACID)** | Strong support for ACID               | Some support ACID (depends on DB)                  |
| **Examples**            | MySQL, PostgreSQL, Oracle, SQL Server | MongoDB, Cassandra, Redis, Couchbase, DynamoDB     |
| **Best For**            | Complex queries, structured data      | Big data, high throughput, flexible schema needs   |
| **Joins**               | Native support                        | Limited or no join support                         |
| **Use Cases**           | ERP, CRM, banking, legacy systems     | Real-time apps, IoT, analytics, content management |


**✅ When to Use SQL (Relational):**
- You need complex joins, strict data integrity, and structured data.
- Ideal for financial systems, HR systems, legacy enterprise apps.

**✅ When to Use NoSQL (Non-Relational):**
- You need flexibility, high scalability, or you're handling semi-structured/unstructured data.
- Great for IoT, mobile apps, product catalogs, and real-time analytics.

---
## 🛠️ Installing MySQL (Step-by-Step Guide)
#### 1. Installing MySQL on Windows : MySQL Installer (GUI)

1. Download Installer
- Go to https://dev.mysql.com/downloads/installer/
- Choose the MySQL Installer (Windows x86, 32-bit)

2. Run Installer
- Select "Developer Default" or "Server only" (based on needs)
- Installer will auto-select MySQL Server, Workbench, Shell, etc.

3. Configure Server
- Choose Config Type: Development / Production
- Set port (default 3306) and root password
-  Add user accounts if needed

4. Complete Installation
- Installer will download and configure all components
- Launch MySQL Workbench or MySQL Shell to connect

#### 🍎 2. Installing MySQL on macOS
```bash
# Install Homebrew (if not already):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


# Install MySQL:
brew install mysql


# Start MySQL Service:
brew services start mysql

# Secure Installation (Set root password):
mysql_secure_installation


# Login to MySQL:
mysql -u root -p

```

#### 🐧 3. Installing MySQL on Ubuntu/Debian (Linux)
```bash
# Update Package Info:
sudo apt update

# Install MySQL Server:
sudo apt install mysql-server


# Secure Installation:
sudo mysql_secure_installation

# Login to MySQL:
sudo mysql -u root -p


# Start/Stop MySQL Service:
sudo systemctl start mysql
sudo systemctl stop mysql


# Check Version:
mysql --version


````

**Connecting with MySQL Shell**
```bash
# check the version
mysql --version

# connect to MySql Server
mysql -u root -p

```

---
## 📌 MySQL Data Types
> MySQL supports a variety of data types grouped into three main categories:

🔢 Numeric Types:
| Type       | Description               |
| ---------- | ------------------------- |
| `INT`      | Integer values            |
| `TINYINT`  | Very small integer        |
| `SMALLINT` | Small integer             |
| `BIGINT`   | Very large integer        |
| `DECIMAL`  | Fixed-point, exact values |
| `FLOAT`    | Approximate decimal       |
| `DOUBLE`   | Double precision float    |

📅 Date and Time Types:
| Type        | Description            |
| ----------- | ---------------------- |
| `DATE`      | YYYY-MM-DD             |
| `DATETIME`  | YYYY-MM-DD HH\:MM\:SS  |
| `TIMESTAMP` | Automatic current time |
| `TIME`      | HH\:MM\:SS             |
| `YEAR`      | Year (YYYY)            |

🔤 String Types:
| Type         | Description                  |
| ------------ | ---------------------------- |
| `CHAR(n)`    | Fixed-length string          |
| `VARCHAR(n)` | Variable-length string       |
| `TEXT`       | Large text                   |
| `BLOB`       | Binary large object (images) |
| `ENUM`       | Predefined value list        |

---

### **🔧 Database-level commands:**
```bash
# 1. CREATE DATABASE
CREATE DATABASE company_db;

# 2. SHOW DATABASES: Lists all databases in the MySQL server.
SHOW DATABASES;

#  3. USE : Selects a database to work with.
USE company_db;


# 4. DROP DATABASE: Deletes an existing database and all its contents. ⚠️ Irreversible – all tables and data in the database are deleted.
DROP DATABASE company_db;

# 5. RENAME DATABASE (Deprecated in newer versions)
-- No direct command. Use dump and restore:
mysqldump -u root -p old_db > old_db.sql
mysql -u root -p -e "CREATE DATABASE new_db"
mysql -u root -p new_db < old_db.sql
mysql -u root -p -e "DROP DATABASE old_db"

# 6. ALTER DATABASE: Changes database-level settings like character set or collation.
ALTER DATABASE company_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 7. SELECT DATABASE()
SELECT DATABASE();

# 8. CREATE SCHEMA (Alias for CREATE DATABASE): Just another way to create a database.
CREATE SCHEMA school_db;
```

---
### 🔧 Table-level commands
**1. CREATE TABLE***
- Creates a new table in the current database.
```sql
CREATE TABLE table_name (
    column1 datatype [constraints],
    column2 datatype [constraints],
    ...
);


CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    hire_date DATE
);

```

** 2. SHOW TABLES**
- Lists all tables in the selected database.
```sql
SHOW TABLES;
```

**3. DESCRIBE / DESC**
- Shows the structure (columns, types, etc.) of a table.
```sql
DESCRIBE employees;
```

**4. DROP TABLE**
- Deletes a table and all its data.
```sql
DROP TABLE table_name;


DROP TABLE employees;
```

**5. RENAME TABLE**
- Changes the name of an existing table.
```sql
RENAME TABLE old_name TO new_name;

RENAME TABLE employees TO staff;
```

**6. ALTER TABLE**
- Used to add, modify, or delete columns or constraints.
```sql
--  Add a column:
ALTER TABLE employees ADD email VARCHAR(100);

--  Modify a column:
ALTER TABLE employees MODIFY name VARCHAR(150);

-- Drop a column:
ALTER TABLE employees DROP COLUMN email;

-- Add a primary key:
ALTER TABLE employees ADD PRIMARY KEY (id);

```

**7. TRUNCATE TABLE**
- Deletes all rows from a table but keeps the structure.
```sql
TRUNCATE TABLE employees;

-- ⚠️ Faster than DELETE, but cannot be rolled back.
```

**8. CREATE TABLE AS**
- Creates a new table using the result of a query.
```sql
CREATE TABLE senior_employees AS
SELECT * FROM employees WHERE hire_date < '2015-01-01';
```

**9. SHOW CREATE TABLE**
- Displays the exact SQL statement used to create the table.
```sql
SHOW CREATE TABLE employees;
```