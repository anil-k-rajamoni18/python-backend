# MCP & Retrieval Pipeline Guide

## 🧠 0. Core Mental Model (Critical for Interviews)

**Retrieval is NOT a function call.**  
**Retrieval is a system capability.**

That's why:
- It must be offline + online
- It must be reusable
- It must be exposed as a tool
- It must be protocol-driven

👉 **MCP exists to formalize this.**

---

## 1️⃣ Online vs Offline Pipelines (WHY this separation exists)

### ❌ Naive (Wrong) Approach

```
User query →
Load documents →
Chunk →
Embed →
Search →
Return results
```

🚨 **Problems:**
- Too slow
- Repeated work
- Not scalable
- Impossible to cache

---

### ✅ Correct Production Architecture

#### 🔹 Offline Pipeline (Heavy, Slow, One-Time)

```
Documents →
Cleaning →
Chunking →
Embedding →
Indexing (FAISS) →
Persist Index
```

#### 🔹 Online Pipeline (Light, Fast, Per Query)

```
User Query →
Embed →
FAISS Search →
Return Top-K
```

📌 **Interview Key Line:**

> "We move all expensive work to offline ingestion."

---

## 2️⃣ Document Ingestion Flow (Real Production Thinking)

### Step-by-Step Flow 🧱

```
Raw Docs
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding
 ↓
Vector Index
```

### 🔍 Why Each Step Exists

#### 📄 Load Documents

- PDFs
- Markdown
- Logs
- Web pages

📌 Garbage in → garbage out

#### ✂️ Chunking (VERY IMPORTANT)

**Why chunk?**
- Embedding models have context limits
- Smaller chunks = better recall
- Large docs dilute meaning

**Typical strategies:**
- Fixed size (300–500 tokens)
- Overlap (10–20%)
- Semantic chunking (advanced)

📌 **Chunking is more important than the model choice.**

#### 🧠 Generate Embeddings

- Same model for all docs
- Normalize vectors
- Deterministic pipeline

#### ⚡ Store in FAISS

- ID → vector
- Metadata stored separately
- Index saved to disk

---

## 3️⃣ Why Retrieval Should Be a Tool (🔥 Interview-Critical)

### ❌ Anti-Pattern

```python
def search(query):
    ...
```

**Problems:**
- Tightly coupled
- Not reusable
- Hard to govern
- No schema enforcement

---

### ✅ Tool-Based Retrieval

```
Agent → Tool Call → Search System → Results
```

**Benefits:**
- Clear contract
- Stateless
- Observable
- Reusable by any agent

📌 **This is exactly why MCP exists.**

---

## 4️⃣ Introduction to MCP Architecture

### What is MCP?

**Model Context Protocol (MCP)** standardizes how models interact with tools.

Think of it as:
- HTTP for tools
- gRPC for AI agents
- OpenAPI for LLM capabilities

### 🧱 MCP High-Level Architecture

```
LLM / Agent (Client)
        ↓
     MCP Client
        ↓
     MCP Server
        ↓
     Tool (Semantic Search)
```

---

## 5️⃣ MCP Core Concepts (You WILL be asked)

### 🔹 MCP Client

- Used by LLM/agent
- Discovers tools
- Sends tool invocation requests
- Receives structured responses

📌 **The model never talks to FAISS directly.**

### 🔹 MCP Server

- Hosts tools
- Owns business logic
- Enforces schemas
- Returns results

📌 **Think of it as a microservice for AI tools.**

### 🔹 Tool Definition

A tool is defined by:
- Name
- Description
- Input schema
- Output schema

This makes tools:
- Discoverable
- Safe
- Self-describing

### 🔹 Input / Output Schemas

**Why schemas matter:**
- Prevent hallucinated inputs
- Enforce types
- Enable validation
- Improve reliability

📌 **Schemas are guardrails for LLMs.**

---

## 6️⃣ Hands-On: Build Semantic Search Ingestion 🛠️

### Step 1️⃣ Load Documents

```python
docs = [
    "Password reset instructions for users",
    "How to update email address",
    "Troubleshooting VPN connection errors"
]
```

### Step 2️⃣ Chunk Text

```python
def chunk(text, size=100):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]
```

📌 Simple chunking is enough to start.

### Step 3️⃣ Generate Embeddings

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, normalize_embeddings=True)
```

### Step 4️⃣ Store in FAISS

```python
import faiss
import numpy as np

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(np.array(embeddings).astype("float32"))
```

### Step 5️⃣ Persist Index

```python
faiss.write_index(index, "docs.faiss")
```

📌 **This completes the OFFLINE pipeline.**

---

## 7️⃣ Build MCP Server: Semantic Search Tool 🧠🔧

### Tool Definition (Conceptual)

**Tool Name:**
```
semantic_search
```

**Input Schema:**
```json
{
  "query": "string",
  "k": "integer"
}
```

**Output Schema:**
```json
{
  "results": [
    {
      "text": "string",
      "score": "number"
    }
  ]
}
```

### Tool Logic (Conceptual Flow)

```
Receive query
 → Embed query
 → FAISS search
 → Fetch metadata
 → Return top-k
```

📌 **LLM never sees FAISS internals.**

---

## 8️⃣ Manual Tool Invocation (Testing 🧪)

**Example input:**

```json
{
  "query": "how do I reset my password?",
  "k": 3
}
```

**Expected output:**

```json
{
  "results": [
    {
      "text": "Password reset instructions for users",
      "score": 0.87
    }
  ]
}
```

📌 **If this works, your semantic search is production-ready.**

---

## 9️⃣ Common Mistakes (Seen in Real Systems ⚠️)

- ❌ Mixing ingestion and query logic
- ❌ Re-embedding documents per query
- ❌ No chunk overlap
- ❌ Tight coupling LLM ↔ FAISS
- ❌ No schema validation

---

## 🔟 Interview Questions You WILL Get 🎤

### Pipelines

**Why separate offline and online pipelines?**  
→ Latency, scalability, cost

**What happens when documents update?**  
→ Re-ingestion + re-indexing

### MCP & Tools

**Why expose retrieval as a tool?**  
→ Reusability, safety, observability

**What problem does MCP solve?**  
→ Standardized model-tool interaction

### Design

**Why FAISS behind MCP instead of direct calls?**  
→ Decoupling, security, versioning

**How do you add access control?**  
→ MCP server layer

---

## 🧠 Final Mental Model (Memorize This)

**Embeddings give meaning**  
**Indexes give speed**  
**BM25 gives precision**  
**MCP gives structure**

---

## ✅ Outcome Achieved

- ✔ You understand full semantic search pipelines
- ✔ You can design offline + online systems
- ✔ You can expose retrieval as an MCP tool
- ✔ You are senior-level interview ready