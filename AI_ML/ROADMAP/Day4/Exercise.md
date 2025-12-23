# 🔹 DAY 4 — Hands-On Real-Time Projects
## Semantic Search Pipeline + MCP Server 🧠🔌

### Mental model for today
> "Search is not an algorithm. Search is a system."

By the end of these projects, you should be able to defend your design choices in interviews, not just run code.

---

## 🧩 Project 1: Offline Semantic Indexing Pipeline (Foundational)

### 🎯 Problem Statement

You have 10,000+ documents (PDFs / markdown / logs).  
You cannot embed on every query → too slow, too expensive.

**You need an offline ingestion pipeline.**

### WHY this project matters (Interview Angle)

Interviewers want to hear:
- Why embeddings are precomputed
- Why ingestion ≠ querying
- How pipelines scale independently

❌ **Junior answer:** "I embed documents and search"

✅ **Senior answer:** "I separate ingestion and retrieval pipelines"

### 🏗️ Architecture (Think Before Code)

```
Raw Docs
   ↓
Loader
   ↓
Chunker
   ↓
Embedding Model
   ↓
Vector Index (FAISS)
   ↓
Persist to Disk
```

### 🛠️ Step-by-Step Implementation (Conceptual)

#### 1️⃣ Load Documents (Offline Job)

**Why**
- Documents change slowly
- Queries happen frequently

**Design Decisions**
- File system / S3 / DB
- Metadata attached (doc_id, source, timestamp)

📌 **Interview follow-up:**

*Why keep metadata outside FAISS?*  
👉 FAISS stores vectors, not rich metadata

#### 2️⃣ Chunk Text (Critical Step ⚠️)

**Why chunking exists**
- Embedding models have context limits
- Retrieval granularity matters

**Rules of Thumb**
- 300–600 tokens per chunk
- Overlap: 10–20%

**Tradeoff**
- Smaller chunks → better recall, worse precision
- Larger chunks → better context, worse matching

📌 **Interview trap:**

*"Why not embed full documents?"*  
👉 Because semantic dilution kills relevance

#### 3️⃣ Generate Embeddings

**Key Concepts**
- Deterministic embeddings
- Same model for docs & queries

**Offline Batch Mode**
- GPU preferred
- Parallelized

📌 **Interview question:**

*What happens if you change embedding models?*  
👉 Full re-index required (vector space mismatch)

#### 4️⃣ Store in FAISS

**Index Choice (Start Simple)**
- IndexFlatIP or IndexFlatL2

**Why Flat first**
- Exact search
- Easy debugging
- Baseline metrics

📌 **Senior insight:**  
Always build Flat index first → then optimize

#### 5️⃣ Persist Index to Disk 💾

**Why persistence matters**
- Cold start recovery
- No re-embedding on restart

**Artifacts**
- `index.faiss`
- `metadata.json`

📌 **Interview question:**

*Why separate vector index and metadata store?*  
👉 Performance + flexibility

### ✅ Outcome

You now have a production-style ingestion pipeline.

---

## 🧩 Project 2: Online Semantic Retrieval as a Tool (Core Project)

### 🎯 Problem Statement

You want LLMs or agents to query semantic search without knowing implementation details.

**Retrieval should be a capability, not hardcoded logic.**

### WHY this project matters (System Design 🔥)

Modern systems:
- ChatGPT tools
- Agent frameworks
- RAG platforms

All require:
- 🔧 Retrieval exposed as a tool

### 🧠 Key Insight

**Search ≠ application logic**

Search should be:
- Stateless
- Query-driven
- Reusable

### 🏗️ Architecture

```
User / Agent
   ↓
MCP Client
   ↓
MCP Server
   ↓
Semantic Search Tool
   ↓
FAISS Index
```

### 🛠️ Step-by-Step Implementation

#### 1️⃣ Load FAISS Index (Startup Phase)

**Why at startup**
- Avoid disk IO per query
- Memory-resident index = low latency

📌 **Interview follow-up:**

*What if index is too big for RAM?*  
👉 Memory-mapped FAISS or sharded indexes

#### 2️⃣ Define Tool Interface (Critical MCP Concept)

**Tool = contract, not code.**

**semantic_search**

**Input:**
- `query`: string
- `k`: int

**Output:**
- text
- score
- metadata

📌 **Interview insight:**  
Schemas enable validation + tooling introspection

#### 3️⃣ Implement Query Flow

**Query Pipeline**

```
Query text
 → Embed
 → FAISS search
 → Fetch metadata
 → Return structured results
```

**Why embed online**
- Queries are dynamic
- Low volume vs documents

📌 **Tradeoff question:**

*Cache query embeddings?*  
👉 Only if query repetition is high

#### 4️⃣ MCP Server Execution

**Responsibilities**
- Accept tool calls
- Validate input schema
- Execute search
- Return output schema

📌 **Senior mindset:**  
MCP Server = microservice for cognition

#### 5️⃣ Manual Tool Testing

Before agents:
- Call tool directly
- Inspect scores
- Verify ranking logic

📌 **Interview trick:**  
Always validate retrieval before generation

### ✅ Outcome

You now expose semantic search as a protocol-based capability.

---

## 🧩 Project 3: Semantic Search Failure Analysis (Advanced)

### 🎯 Problem Statement

Semantic search fails silently.

**You must diagnose retrieval quality.**

### Experiments to Run

#### 🔍 Case 1: Exact Keyword Missing

**Query:** "HTTP 504 error"  
**Semantic result:** Talks about timeouts but misses error code

👉 Keyword search would win

#### 🔍 Case 2: Synonym Match

**Query:** "payment failure"  
Keyword search fails  
Semantic search succeeds

#### 🔍 Case 3: Long Queries

Semantic may over-generalize

### Key Lesson 🧠

**No single retrieval strategy wins always**

This justifies:

👉 **Hybrid Search (BM25 + Vectors)**

---

## 🔥 Interview Questions & Model Answers

### 1️⃣ Why retrieval should be a tool?

**Answer**
- Decouples search from application logic
- Enables agents, workflows, reuse
- Easier A/B testing & upgrades

### 2️⃣ Online vs Offline pipelines?

| Aspect    | Offline      | Online       |
|-----------|--------------|--------------|
| Latency   | High         | Low          |
| Frequency | Rare         | Frequent     |
| Cost      | Batch        | Per request  |
| Examples  | Indexing     | Querying     |

### 3️⃣ Why MCP over REST?

**Senior Answer**
- Schema-first
- Tool introspection
- Agent-friendly
- Less glue code

### 4️⃣ What breaks semantic search?

- Poor chunking
- Wrong embedding model
- Domain mismatch
- No hybrid fallback

### 5️⃣ How would you scale this?

- Shard FAISS by domain
- Async ingestion
- Cache frequent queries
- Add BM25 reranker

### 6️⃣ What's the biggest production mistake?

❌ **Treating search as a feature**  
✅ **Treating search as infrastructure**