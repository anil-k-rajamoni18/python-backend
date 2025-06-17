# 🎯 Session 01: Java Fundamentals

---

## 🧩 What is a Programming Language?
- A way for humans to give **instructions to a computer**.
- A **program** is a set of instructions to perform a specific task.
- A **language** has grammar and vocabulary to form correct and efficient instructions.

---

## 🧱 Language Types

### 💻 Machine Language
- Binary code (0s and 1s) directly understood by the CPU.
- **Low-level**, hardware-specific, hard to read/write manually.

### 🛠 Assembly Language
- Uses **mnemonics** (e.g., `MOV AX, 1`) instead of binary.
- More readable than machine language; still hardware-close.

### 🌐 High-Level Language
- Closer to human languages — includes loops, variables, functions.
- Examples: **Java**, **Python**, **C++**.

---

## ☕ What is Java?
- A **high-level**, **object-oriented** language + platform.
- Portable, secure, and robust.
- Created by **Sun Microsystems** in **1995**; now maintained by **Oracle**.
- Runs on 3+ billion devices: mobile, desktop, web, servers, games, IoT, etc.

---

## 📜 History of Java
- 1991: Began as "Green Project" → language named **Oak**
- 1995–96: Released as **Java 1.0**
- Name changed due to trademark; "Java" chosen (Indonesian coffee island)
  
---

## 🧰 Java Terminology

### 🧩 JDK (Java Development Kit)
- Full development kit: compiler (`javac`), debugger, libraries, etc.

### 🧩 JRE (Java Runtime Environment)
- Includes **JVM** and core libraries to **run** Java programs.

### 🧩 JVM (Java Virtual Machine)
- Executes Java **bytecode**, converting it to machine code.
- Enables **platform independence**.

### 🧩 Bytecode
- Intermediate code (`.class`) produced by `javac`; executed by JVM.

### 🧩 ClassPath
- Paths/directories/JARs that JVM/compiler uses to locate classes.
- Configurable via `-cp` or `CLASSPATH` env variable.

### 🧩 Garbage Collector (GC)
- Automatically **frees memory** of unused objects to avoid memory leaks.

---

## ✅ Key Java Features
- 🔒 **Platform independence** — Write Once, Run Anywhere (WORA)
- 🧱 **Object-Oriented** — Promotes modularity and reuse
- ✅ **Simple** — No pointers, simpler to learn
- 🛡 **Secure** — Bytecode verification, sandboxing
- 🏗 **Robust** — Strong typing, exception handling, memory safety
- 🔄 **Multithreaded** — Built-in concurrency support
- ⚡ **High-performance** — JIT compiler optimizes runtime
- 🌐 **Dynamic** — Runtime class loading, reflection
- 🔗 **Distributed-ready** — Networking libraries included

---

## 💻 Sample Program

```java
package com.example.helloworld;

import java.util.Date;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Current Date: " + new Date());
    }
}
```

