# Legacy Project Understanding — AI Prompts

Here's a comprehensive set of prompts organized by category:

---

## 🏗️ Architecture & Structure

```
"Analyse this package/folder structure and infer the likely architecture pattern 
(MVC, layered, domain-driven). What are the key modules and how do they relate?"
```

```
"Looking at this codebase, identify the main architectural layers and draw 
boundaries between them. Where are those boundaries violated?"
```

```
"What design patterns are used in this class/module? Are they implemented 
correctly, and do they introduce any coupling risks?"
```

```
"Map the dependency graph of this module. Which classes/packages does it depend 
on, and which depend on it? Identify the most tightly coupled areas."
```

---

## 🔍 Code Comprehension

```
"Explain what this class does in plain English. What is its single responsibility? 
If it has more than one, list them all."
```

```
"Trace the full execution path for [feature/use case] from the entry point 
(HTTP request / EJB call / MQ message) all the way to the database. 
List every class, method, and external call involved."
```

```
"What would break if I deleted [ClassName]? List every class that directly 
or transitively depends on it."
```

```
"This method is [N] lines long. Break it down step by step. What is each 
block doing, and what should each block ideally be extracted into?"
```

```
"Identify all side effects this method produces — what does it mutate, 
what external systems does it touch, what state does it change?"
```

---

## 🗄️ Database & Data Access

```
"List every SQL query or stored procedure call in this class/module. 
Which tables does it read from and write to? Are there any cross-module queries 
that suggest shared state or missing service boundaries?"
```

```
"Analyse this database schema. Which tables belong together logically? 
Suggest how to group them into bounded contexts / microservices domains."
```

```
"Identify all stored procedures and triggers in this schema. For each one, 
explain what business logic it encodes and whether it should live in the 
application layer instead."
```

```
"Where is this entity mutated across the codebase? List every class and method 
that writes to [TableName]. Are there race conditions or concurrency risks?"
```

```
"Are there any N+1 query patterns in this code? Where is lazy loading 
used unsafely?"
```

---

## 🔗 Integration & External Dependencies

```
"Identify all external system integrations in this module — REST endpoints, 
SOAP services, MQ queues, FTP, SMTP, LDAP. For each, describe what data 
is exchanged and what happens if that system is unavailable."
```

```
"Analyse this WSDL and explain the operations, input/output types, and 
expected behaviors. What Java classes would be generated from this? 
What's the equivalent REST API design?"
```

```
"Where are external HTTP/SOAP calls made without a timeout, retry, or 
circuit breaker? List all such callsites — these are reliability risks."
```

```
"What are all the third-party and internal libraries used in pom.xml / build.gradle? 
For each internal/org library, explain what it provides and whether a 
standard Spring Boot or Java equivalent exists."
```

---

## ⚡ Transactions & Consistency

```
"Identify all transaction boundaries in this code. Are they using JTA, BMT, CMT, 
or Spring @Transactional? Where could a partial failure leave data inconsistent?"
```

```
"Which operations in this module need to be atomic? Where are distributed 
transactions used — and are they actually necessary, or can they be 
replaced with eventual consistency?"
```

```
"List all places where data is written to more than one table or system 
in a single operation. What is the rollback behavior if the second write fails?"
```

---

## 🧩 Domain & Bounded Contexts

```
"Looking at the package structure, class names, and method names, group these 
into logical business domains. Suggest which groups would make good microservice 
candidates and explain why."
```

```
"Which classes/modules are referenced from everywhere? These are likely 
'god objects' or shared utilities. Should they be a shared library, 
or are they hiding a missing domain concept?"
```

```
"For [Module/Feature], describe the business process it implements end-to-end 
in non-technical language. Who are the actors? What are the steps? 
What are the business rules?"
```

```
"Where is business logic leaking into the wrong layer — e.g., business rules 
in JSP/UI, SQL logic in controllers, or presentation formatting in service classes?"
```

---

## 🔒 Security & Auth

```
"How is authentication and authorization implemented? Is it container-managed 
(WebSphere JAAS), Spring Security, or custom? What roles/permissions exist 
and where are they enforced?"
```

```
"Find all places where user input reaches a SQL query, file path, shell command, 
or XML parser without sanitization. List potential injection vulnerabilities."
```

```
"Where are secrets, passwords, and API keys stored? Are any hardcoded in source 
code or property files committed to version control?"
```

---

## 🔄 State & Concurrency

```
"Identify all static variables, singletons, and application-scoped beans. 
What mutable shared state exists? Could this cause thread-safety issues 
when running multiple instances?"
```

```
"Are there any caching mechanisms (EhCache, custom maps, static caches)? 
What is cached, for how long, and how is it invalidated? 
What breaks if a second service instance has a stale cache?"
```

```
"Find all use of synchronized, volatile, ThreadLocal, or locks. 
Are these correct? Are there potential deadlocks?"
```

---

## 🧪 Testing & Quality

```
"What test coverage exists for this class? Identify which branches, 
edge cases, and error paths have no tests. Suggest the 5 most important 
test cases to write before migrating this code."
```

```
"Write a characterization test (golden master / approval test) for this method 
that captures its current behavior exactly — so any regression during 
migration is immediately visible."
```

```
"Rate the migration complexity of this class from 1–10. Explain what makes 
it hard to migrate and suggest the safest migration approach."
```

---

## 🖥️ UI / JSP Analysis

```
"Analyse this JSP page and its backing bean/servlet. What data does it display? 
What user actions does it support? Map each piece of data to a REST API endpoint 
and each action to an HTTP method + URL."
```

```
"What business logic is embedded in this JSP (scriptlets, JSTL conditions, 
tag libraries)? Should this logic live in the API or the React component?"
```

```
"List all session attributes this JSP reads. Which of these are needed 
across pages (true session state) vs. which are just request-scoped data 
that should be an API response field?"
```

---

## 🚀 Migration Readiness

```
"Given this class, what are the migration steps to convert it to a 
Spring Boot 3 / Java 21 equivalent? Flag any javax.* → jakarta.* changes, 
WebSphere-specific APIs, and EJB dependencies that need replacing."
```

```
"If I extract [Module] into a standalone microservice, what are all the 
things it currently relies on from the monolith that I would need to 
replace with API calls or events?"
```

```
"What would a zero-downtime migration strategy look like for this feature? 
How would I run both the old monolith path and new microservice path 
in parallel using feature flags?"
```

```
"Generate a risk register for migrating this module. What are the top 5 risks, 
their likelihood, their impact, and a suggested mitigation for each?"
```

---

> 💡 **Pro tip:** Always paste the relevant code directly into the prompt for best results. The more context you provide (class + its dependencies + the DB schema it touches), the more precise and actionable the analysis will be.
