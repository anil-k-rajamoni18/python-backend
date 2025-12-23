# 🚀 DAY-2 Hands-On Real-Time Projects
## Vector Databases & FAISS Indexing

---

## 🟢 PROJECT 1: Large-Scale Semantic FAQ Search (FAISS Flat → IVF)

### 📌 Business Problem

Customer support has 500K+ FAQs.  
Brute-force search is too slow.

**Goal:**  
➡️ Low-latency semantic retrieval at scale

### 🧠 Concepts Applied

- FAISS architecture
- Flat vs IVF
- Index training
- Vector persistence
- Recall vs latency tradeoff

### 🏗️ High-Level Architecture

```
User Query
   ↓
Embedding Model
   ↓
FAISS Index (IVF)
   ↓
Top-K FAQ IDs
   ↓
Metadata DB
```

### 🛠️ Step-by-Step Implementation

#### Step 1️⃣ Generate / Load Embeddings

```python
import numpy as np

dimension = 384
faq_vectors = np.random.rand(500000, dimension).astype("float32")
```

📌 In production: embeddings are precomputed offline

#### Step 2️⃣ Start with Flat Index (Baseline)

```python
import faiss

flat_index = faiss.IndexFlatIP(dimension)
flat_index.add(faq_vectors)
```

- ✔ Exact results
- ❌ Too slow for 500K+

#### Step 3️⃣ Upgrade to IVF Index

```python
nlist = 4096   # number of clusters
quantizer = faiss.IndexFlatIP(dimension)
ivf_index = faiss.IndexIVFFlat(quantizer, dimension, nlist)
```

#### Step 4️⃣ Train the Index

```python
ivf_index.train(faq_vectors)
ivf_index.add(faq_vectors)
```

📌 Training learns vector space structure

#### Step 5️⃣ Tune Search

```python
ivf_index.nprobe = 16
```

⚖️ **Tradeoff:**
- Low nprobe → faster, less recall
- High nprobe → slower, better recall

#### Step 6️⃣ Query

```python
query = np.random.rand(1, dimension).astype("float32")
scores, ids = ivf_index.search(query, k=5)
```

### 🎤 Interview Talking Points

- Why IVF over Flat?
- How do you choose nlist?
- What happens if distribution changes?
- How do you measure recall loss?

---

## 🟡 PROJECT 2: Real-Time Product Recommendation Engine (HNSW)

### 📌 Business Problem

E-commerce site:
> "Show similar products instantly while user browses"

**Latency budget:** < 20ms

### 🧠 Concepts Applied

- HNSW indexing
- Memory vs speed
- Graph-based ANN
- Real-time constraints

### 🏗️ Architecture

```
Product Embeddings
   ↓
HNSW Index (RAM)
   ↓
Nearest Neighbors
```

### 🛠️ Step-by-Step Implementation

#### Step 1️⃣ Create HNSW Index

```python
index = faiss.IndexHNSWFlat(dimension, 32)
```

32 → graph connectivity (M)

#### Step 2️⃣ Add Vectors

```python
index.add(faq_vectors)
```

📌 No training required

#### Step 3️⃣ Tune Search Depth

```python
index.hnsw.efSearch = 64
```

⚖️ Higher efSearch → better recall, more RAM

#### Step 4️⃣ Query

```python
scores, ids = index.search(query, 5)
```

### 🧠 Why HNSW Here?

- Extremely fast
- Excellent recall
- Ideal for online search

### 🎤 Interview Talking Points

- IVF vs HNSW?
- Why HNSW uses more memory?
- What happens as index grows?
- When NOT to use HNSW?

---

## 🔵 PROJECT 3: Persistent Vector Store (Save / Load FAISS)

### 📌 Problem

Indexes take hours to build.  
You cannot rebuild on every restart.

### 🧠 Concepts Applied

- Vector persistence
- Cold start optimization
- Production reliability

### 🛠️ Steps

#### Step 1️⃣ Save Index

```python
faiss.write_index(index, "products_hnsw.faiss")
```

#### Step 2️⃣ Load Index at Startup

```python
index = faiss.read_index("products_hnsw.faiss")
```

📌 **Typical production flow:**

Server start → Load FAISS → Ready in seconds

### 🎤 Interview Insight

> FAISS is a library, not a database.  
> Persistence is your responsibility.

---

## 🔴 PROJECT 4: Hybrid Retrieval System (BM25 + FAISS)

### 📌 Business Problem

Some queries:
- Are keyword-heavy
- Contain numbers, IDs, codes
- Embeddings alone fail.

### 🏗️ Architecture

```
Query
  ├── BM25 → Top-K₁
  └── FAISS → Top-K₂
        ↓
Merge + Rerank
```

### 🧠 Concepts Applied

- Hybrid search
- Recall optimization
- Practical relevance tuning

### 🛠️ Steps (Conceptual)

1. BM25 retrieves keyword matches
2. FAISS retrieves semantic matches
3. Union results
4. Rerank (optional cross-encoder)

📌 **This is how real search systems work**

### 🎤 Interview Gold Answer 🏆

> "We combine lexical and semantic retrieval to maximize recall."

---

## 🧠 Common Pitfalls (Very Important ⚠️)

- ❌ Using Flat index for millions of vectors
- ❌ Forgetting to train IVF index
- ❌ Using wrong distance metric
- ❌ No persistence strategy
- ❌ Ignoring memory limits

---

## 🎯 Interview Question Bank (WITH ANSWER HINTS)

### FAISS Basics

**Why do we need ANN indexes?**  
→ Brute force is O(N×D)

**What does FAISS store?**  
→ Vectors + IDs, not metadata

### Indexing

**Flat vs IVF vs HNSW?**  
→ Accuracy vs speed vs memory

**What is nprobe?**  
→ Number of clusters searched

**Does HNSW need training?**  
→ No

### System Design

**How would you index 100M vectors?**  
→ IVF/HNSW + sharding

**How do you handle index updates?**  
→ Batch rebuild or incremental add

### Production

**How do you persist FAISS?**  
→ write_index / read_index

**How do you tune recall vs latency?**  
→ nprobe / efSearch

---

## 🧠 Summary

**FAISS makes similarity search feasible by searching less, not faster math.**

- **Flat** → search everything
- **IVF** → search clusters
- **HNSW** → walk graph