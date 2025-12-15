# 15-Day Search & MCP Mastery Roadmap

## 🎯 Overall Objective (What You'll Achieve)

By the end of this roadmap, you will be able to:

- Design semantic, keyword, and hybrid search systems
- Build end-to-end ingestion → retrieval → reranking pipelines
- Evaluate search systems using offline and online metrics
- Implement MCP-based modular AI systems
- Use MCP Registry for dynamic tool discovery
- Build production-ready RAG & conversational systems
- Deploy everything using Docker & Kubernetes
- Explain system design decisions confidently in interviews

## 🧠 Foundational Concepts You Will Master

- Embeddings & vector similarity
- Vector databases (FAISS)
- Keyword search (BM25)
- Hybrid search strategies
- Query expansion
- Reranking (cross-encoders)
- Search evaluation
- MCP (Model Context Protocol)
- MCP Registry & tool discovery
- RAG (Retrieval Augmented Generation)
- Memory & feedback loops
- Kubernetes deployment

---

## 🗓️ 15-Day Detailed Roadmap (Day-Wise)

### 🟢 DAYS 1–3: Core Foundations (Absolutely Critical)

#### 🔹 DAY 1 — NLP & Embeddings Fundamentals

**Topics to Learn**
- What embeddings are
- Dense vs sparse representations
- Word embeddings vs sentence embeddings
- Bi-encoders vs cross-encoders
- Cosine similarity, dot product, Euclidean distance
- Embedding normalization
- Popular models:
  - Sentence-BERT
  - MiniLM
  - E5

**Hands-On Tasks**
- Load a sentence-transformer model
- Generate embeddings for sample sentences
- Compute cosine similarity
- Compare:
  - Similar sentences
  - Unrelated sentences

**Outcome**
✅ You can clearly explain why semantic search works

---

#### 🔹 DAY 2 — Vector Databases & Indexing

**Topics to Learn**
- Why vector databases are needed
- FAISS architecture
- Index types:
  - Flat
  - IVF
  - HNSW
- Index training vs querying
- Memory vs disk storage
- Vector persistence

**Hands-On Tasks**
- Create FAISS index
- Add embeddings
- Perform top-k similarity search
- Save & load index from disk

**Outcome**
✅ You understand fast similarity search at scale

---

#### 🔹 DAY 3 — Keyword Search & BM25

**Topics to Learn**
- TF-IDF vs BM25
- Tokenization
- Inverted index
- Precision vs recall tradeoffs
- Why keyword search still matters

**Hands-On Tasks**
- Index documents using Elasticsearch or Python BM25
- Run keyword queries
- Analyze failures compared to semantic search

**Outcome**
✅ You can justify hybrid search architectures

---

### 🟡 DAYS 4–6: Semantic + Hybrid Search (With MCP)

#### 🔹 DAY 4 — Semantic Search Pipeline + MCP Server

**Topics to Learn**
- Online vs offline pipelines
- Document ingestion flow
- Why retrieval should be a tool
- Introduction to MCP architecture
- MCP Concepts:
  - MCP Client
  - MCP Server
  - Tool definitions
  - Input/output schemas

**Hands-On Tasks**
- Build ingestion script:
  - Load documents
  - Chunk text
  - Generate embeddings
  - Store embeddings in FAISS
- Build MCP Server:
  - Tool: `semantic_search(query, k)`
  - Test tool invocation manually

**Outcome**
✅ Semantic search exposed as a protocol-based capability

---

#### 🔹 DAY 5 — Hybrid Search System

**Topics to Learn**
- Why semantic alone is insufficient
- Score normalization techniques
- Weighted scoring
- Query intent detection

**MCP Tools**
- `semantic_search`
- `keyword_search`
- `hybrid_rank`

**Hands-On Tasks**
- Retrieve results from:
  - FAISS
  - BM25
- Normalize scores
- Combine using weighted sum
- Expose hybrid ranking as MCP tool

**Outcome**
✅ You can design hybrid search systems

---

#### 🔹 DAY 6 — Query Expansion

**Topics to Learn**
- Static synonyms
- Embedding-based expansion
- LLM-based expansion
- Tradeoffs: precision vs recall

**MCP Tool**
- `expand_query(query)`

**Hands-On Tasks**
- Expand queries using embedding similarity
- Merge expanded queries
- Cache expansions
- Measure recall improvement

**Outcome**
✅ Improved recall without damaging relevance

---

### 🟠 DAYS 7–9: Reranking, Feedback & Evaluation

#### 🔹 DAY 7 — Reranking (Two-Stage Retrieval)

**Topics to Learn**
- Bi-encoder vs cross-encoder
- Reranking architecture
- Latency vs accuracy tradeoffs

**MCP Tool**
- `rerank_results(query, documents)`

**Hands-On Tasks**
- Retrieve top-10 from FAISS
- Rerank using cross-encoder
- Compare ranking before & after

**Outcome**
✅ You understand production-grade retrieval pipelines

---

#### 🔹 DAY 8 — Offline Search Evaluation

**Topics to Learn**
- Ground truth creation
- Precision@k
- Recall@k
- MRR
- NDCG

**Hands-On Tasks**
- Create labeled queries
- Evaluate:
  - Keyword search
  - Semantic search
  - Hybrid search
- Compare metrics

**Outcome**
✅ You can prove relevance improvements

---

#### 🔹 DAY 9 — Online Evaluation & Feedback

**Topics to Learn**
- Click-through rate
- Dwell time
- Explicit vs implicit feedback
- A/B testing

**MCP Tools**
- `log_click`
- `log_feedback`
- `boost_document`

**Hands-On Tasks**
- Log user interactions
- Boost documents using feedback
- Rerun evaluation

**Outcome**
✅ Search improves using real user signals

---

### 🔵 DAYS 10–12: MCP + RAG + Memory

#### 🔹 DAY 10 — Ingestion Pipelines (System Design)

**Topics to Learn**
- Batch vs streaming ingestion
- Cron vs Airflow vs Celery
- Why ingestion should be decoupled

**Hands-On Tasks**
- Separate ingestion service
- Run scheduled embedding jobs
- Version embeddings

**Outcome**
✅ Clean, scalable ingestion architecture

---

#### 🔹 DAY 11 — LangChain + MCP

**Topics to Learn**
- Agents
- Tools
- Memory
- Prompt templates

**Hands-On Tasks**
- Build agent
- Discover MCP tools dynamically
- Use multiple MCP servers

**Outcome**
✅ No hard-coded tool logic

---

#### 🔹 DAY 12 — Memory & Context Management

**Topics to Learn**
- Short-term vs long-term memory
- Redis memory
- User context isolation

**MCP Server**
- Memory provider

**Hands-On Tasks**
- Persist chat memory
- Retrieve past context
- Inject into prompts

**Outcome**
✅ Stateful conversational AI

---

### 🔴 DAYS 13–15: Deployment & System Design

#### 🔹 DAY 13 — Docker & Kubernetes

**Topics to Learn**
- Containerizing MCP servers
- Resource limits
- Secrets
- RBAC

**Hands-On Tasks**
- Deploy MCP Registry
- Deploy search + memory servers
- Expose via ingress

**Outcome**
✅ Production-ready deployment

---

#### 🔹 DAY 14 — System Design (Search Platform)

**Topics to Learn**
- End-to-end architecture
- Bottlenecks
- Scaling strategies
- Cost optimization

**Hands-On Tasks**
- Whiteboard design
- Identify failure points
- Optimize latency

**Outcome**
✅ Architect-level explanations

---

#### 🔹 DAY 15 — Mock Interviews & Refinement

**Tasks**
- Re-answer interview questions
- Time responses
- Polish explanations

**Outcome**
✅ Confident & structured answers

---

## 🚀 Detailed Project Implementation Steps

### 🟢 PROJECT 1: MCP-Based Hybrid Search Engine

**Steps**
1. Collect dataset
2. Chunk documents
3. Generate embeddings
4. Store in FAISS
5. Implement BM25
6. Expose search tools via MCP
7. Combine scores
8. Add evaluation metrics
9. Deploy MCP Registry
10. Test agent-driven search

---

### 🟡 PROJECT 2: Legal Document Search with Reranking

**Steps**
1. Ingest legal docs
2. Build semantic search MCP server
3. Implement reranker MCP tool
4. Add query expansion
5. Evaluate ranking quality
6. Optimize latency

---

### 🔴 PROJECT 3: Conversational RAG with MCP Memory

**Steps**
1. Chunk documents
2. Embed and store vectors
3. Build retrieval MCP server
4. Add Redis memory MCP server
5. Build agent
6. Enable feedback logging
7. Deploy on Kubernetes

---

## 🎤 Final Takeaway

**You're not just learning tools. You're learning how to design AI systems properly.**

This roadmap takes you from:

> "I know embeddings"

to

> "I can design and deploy modular AI platforms using MCP."