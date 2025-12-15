# MCP-Based Search Projects Implementation Guide

## 🟢 PROJECT 1: MCP-Based Hybrid Search Engine
### (Semantic + Keyword + MCP + Evaluation)

---

### 1️⃣ Project Overview

**Objective**

Build a production-ready hybrid search engine that:
- Supports semantic search (meaning-based)
- Supports keyword search (exact match)
- Combines both using hybrid scoring
- Exposes all search capabilities via MCP tools
- Is consumable by agents dynamically via MCP Registry

---

### 2️⃣ System Architecture

**High-Level Components**

```
User / Agent
     |
     v
MCP Registry
     |
     v
Hybrid Search MCP Server
     |            |
     |            |
Semantic Tool   Keyword Tool
 (FAISS)        (BM25)
```

---

### 3️⃣ Dataset Collection

**Data Type**

Product descriptions / articles / FAQs (any text corpus)

Each record should have:
- `doc_id`
- `title`
- `content`
- optional metadata (category, tags)

**Dataset Sources**
- Wikipedia dumps
- Public FAQs
- Company docs
- Kaggle datasets

**Output**

A normalized dataset in JSON or CSV:

```json
{
  "id": "doc_123",
  "text": "This document explains refund policies..."
}
```

---

### 4️⃣ Document Chunking

**Why Chunking?**
- Transformer models have token limits
- Smaller chunks improve retrieval precision

**Chunking Strategy**
- Chunk size: 300–500 tokens
- Overlap: 50–100 tokens

**Output**

Each chunk should store:
- `chunk_id`
- `doc_id`
- `chunk_text`

---

### 5️⃣ Embedding Generation

**Model**

Sentence-BERT / MiniLM / E5

**Process**
1. Load embedding model
2. Generate embeddings for each chunk
3. Normalize embeddings (important for cosine similarity)

**Output**

```
embedding: List[float]
```

---

### 6️⃣ Vector Storage (FAISS)

**FAISS Index**
- Start with `IndexFlatIP` (cosine similarity)
- Later upgrade to IVF or HNSW

**Stored Mapping**

```json
{
  "vector_id": 45,
  "chunk_text": "...",
  "doc_id": "doc_123"
}
```

**Persistence**
- Save index to disk
- Reload during service startup

---

### 7️⃣ Keyword Search (BM25)

**Why BM25?**
- Captures exact terms
- Essential for proper nouns, IDs, legal terms

**Implementation**
- Elasticsearch OR
- Python BM25 library

**Output**

```json
{
  "doc_id": "doc_123",
  "bm25_score": 12.4
}
```

---

### 8️⃣ MCP Tool Design

**MCP Server: Hybrid Search**

#### Tool 1 — Semantic Search

```json
{
  "name": "semantic_search",
  "input": { "query": "string", "top_k": "int" },
  "output": { "results": "list" }
}
```

#### Tool 2 — Keyword Search

```json
{
  "name": "keyword_search",
  "input": { "query": "string", "top_k": "int" },
  "output": { "results": "list" }
}
```

#### Tool 3 — Hybrid Ranking

```json
{
  "name": "hybrid_search",
  "input": {
    "query": "string",
    "semantic_weight": "float",
    "keyword_weight": "float"
  }
}
```

---

### 9️⃣ Hybrid Scoring Logic

**Score Normalization**
- Normalize semantic and BM25 scores separately
- Avoid dominance of one method

**Final Score**

```
final_score = 
  (semantic_weight × semantic_score)
+ (keyword_weight × bm25_score)
```

---

### 🔟 Evaluation Metrics

**Offline Metrics**
- Precision@k
- Recall@k
- MRR
- NDCG

**Test Dataset**

Manually labeled:

```json
{
  "query": "refund policy",
  "relevant_docs": ["doc_12", "doc_34"]
}
```

---

### 1️⃣1️⃣ MCP Registry Deployment

**Purpose**
- Enables dynamic discovery
- Agents do not hardcode tools

**Registry Stores**
- Tool name
- Input schema
- Endpoint

---

### 1️⃣2️⃣ Agent-Driven Testing

**Flow**
1. Agent queries registry
2. Discovers hybrid search tool
3. Executes tool
4. Interprets results

---

## 🟡 PROJECT 2: Legal Document Search with Reranking

---

### 1️⃣ Project Objective

Build a two-stage retrieval system:
- Fast retrieval (bi-encoder)
- Accurate reranking (cross-encoder)

---

### 2️⃣ Architecture

```
Query
  |
Bi-Encoder Retrieval (FAISS)
  |
Top-K Results
  |
Cross-Encoder Reranker
  |
Final Ranked Results
```

---

### 3️⃣ Legal Document Ingestion

**Document Types**
- Contracts
- Policies
- Compliance docs

**Metadata**
- Clause type
- Jurisdiction
- Version

---

### 4️⃣ Semantic Search MCP Server

**Tool**

```
semantic_retrieve(query, k)
```

**Output**
- Top-K candidate chunks

---

### 5️⃣ Reranker MCP Tool

**Model**

Cross-encoder (BERT-based)

**Tool**

```
rerank(query, documents)
```

**Behavior**
- Takes query + each doc
- Produces relevance score
- Reorders results

---

### 6️⃣ Query Expansion

**Methods**
- Static synonyms
- Embedding similarity
- Optional LLM expansion

**MCP Tool**

```
expand_query(query)
```

---

### 7️⃣ Evaluation

**Metrics**
- NDCG (primary)
- MRR
- Precision@5

**Comparison**
- Semantic only
- Hybrid
- Hybrid + reranking

---

### 8️⃣ Latency Optimization

**Techniques**
- Reduce top-k before rerank
- Batch reranking
- Cache embeddings
- Async inference

---

## 🔴 PROJECT 3: Conversational RAG with MCP Memory

---

### 1️⃣ Project Objective

Build a stateful conversational AI that:
- Retrieves documents
- Maintains memory
- Learns from feedback
- Uses MCP for modularity

---

### 2️⃣ System Architecture

```
User
 |
Agent (LangChain)
 |
MCP Registry
 |
---------------------------------
| Retrieval | Memory | Feedback |
---------------------------------
```

---

### 3️⃣ Document Chunking & Embeddings

(Same as Project 1, reused)

---

### 4️⃣ Retrieval MCP Server

**Tool**

```
retrieve_context(query)
```

Returns relevant document chunks

---

### 5️⃣ Redis Memory MCP Server

**Purpose**
- Persist chat history
- Support scaling
- Session isolation

**Tools**

```
get_memory(session_id)
store_memory(session_id, message)
```

---

### 6️⃣ Agent Design

**Agent Responsibilities**
- Decide which tool to call
- Inject memory into prompts
- Generate final response

---

### 7️⃣ Feedback Logging

**Feedback Types**
- Thumbs up/down
- Query re-run
- Clicked context

**MCP Tool**

```
log_feedback(query, doc_id, rating)
```

---

### 8️⃣ Kubernetes Deployment

**Components as Pods**
- Agent service
- Retrieval MCP server
- Memory MCP server
- MCP Registry
- Redis

**Features**
- HPA for agent
- Resource limits for LLM
- Secrets via K8s secrets

---

## 🎯 Final Outcome

After implementing these three projects, you will be able to:

- ✅ Design enterprise-grade search systems
- ✅ Explain retrieval → reranking → feedback loops
- ✅ Use MCP as a first-class architecture
- ✅ Confidently discuss system design & tradeoffs
- ✅ Demonstrate real production thinking