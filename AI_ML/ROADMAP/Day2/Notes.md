# FAISS & Vector Databases Guide

## 🧠 0. Core Mental Model (Before Anything Else)

**Vector databases exist because brute-force search does not scale.**

- 1K vectors → brute force is fine
- 1M vectors → borderline
- 10M–1B vectors → impossible without indexing

📌 **Vector DB = ANN (Approximate Nearest Neighbor) + storage + metadata**

---

## 1️⃣ Why Vector Databases Are Needed

### The Naive Approach (Flat Search 🐢)

```
For each query:
  Compare with every vector
  Sort results
```

⏱ **Time Complexity:** O(N × D)  
(N = number of vectors, D = dimensions)

### Real-World Analogy 🏙️

Searching for a restaurant:

- ❌ Visit every building in the city
- ✅ Use maps, zones, shortcuts

➡️ **Vector indexes organize space so we don't search everything.**

### What Vector DBs Actually Solve

- Fast similarity search (ANN)
- Persistence (save/load)
- Metadata filtering (usually external)
- Horizontal scalability (in production)

📌 **FAISS focuses on ANN, not metadata.**

---

## 2️⃣ FAISS Architecture (Think in Layers 🧱)

### High-Level View

```
Embeddings
   ↓
FAISS Index (ANN)
   ↓
Top-K Vector IDs
   ↓
Metadata Store (DB)
```

### Key FAISS Concepts

- **Index** → search strategy
- **Quantizer** → space partitioning
- **Distance metric** → cosine / L2
- **Search params** → speed vs accuracy

📌 **FAISS does not store text—only vectors + IDs.**

---

## 3️⃣ Index Types (🔥 Very Interview-Critical)

### 🔹 IndexFlat (Brute Force but Optimized)

#### What It Is

- Stores all vectors
- Compares query with every vector

```python
faiss.IndexFlatIP(dimension)
```

#### Pros

- ✅ Exact results
- ✅ No training
- ✅ Simple

#### Cons

- ❌ Slow for large N
- ❌ High memory

#### When to Use

- ≤100K vectors
- Baseline evaluation
- Ground truth generation

📌 **Interview Tip:** Flat = gold standard for accuracy comparison.

---

### 🔹 IVF (Inverted File Index)

#### Mental Model 🗂️

Like library shelves:
1. First choose shelf
2. Then search books on that shelf only

#### How IVF Works

1. Cluster vectors (k-means)
2. Assign vectors to clusters
3. Query searches few clusters only

**IndexIVFFlat**

#### Key Parameters

- `nlist` → number of clusters
- `nprobe` → clusters searched per query

#### ⚖️ Tradeoff:

Higher nprobe → better recall, slower search

#### Pros / Cons

**Pros:**
- ✅ Much faster than Flat
- ✅ Memory efficient

**Cons:**
- ❌ Requires training
- ❌ Approximate

#### Interview Insight 🧠

> IVF trades recall for speed by reducing search space.

---

### 🔹 HNSW (Graph-Based Index 🔥)

#### Mental Model 🕸️

Vectors form a multi-layer small-world graph.  
Search walks the graph greedily.

#### Why HNSW Is Powerful

- Logarithmic search complexity
- Excellent recall
- No clustering step

#### Key Parameters

- `M` → graph connections
- `efSearch` → search depth
- `efConstruction` → build quality

#### ⚖️ Tradeoff:

Higher ef → better recall, more RAM

#### Pros / Cons

**Pros:**
- ✅ Fast + accurate
- ✅ Great for real-time search

**Cons:**
- ❌ High memory
- ❌ Slower index build

#### Interview Gold 🏆

> HNSW is often the default choice for real-time semantic search.

---

## 4️⃣ Index Training vs Querying (Often Confused ❌)

### Training Phase

- Learns structure (clusters / centroids)
- Happens once
- Required for IVF, PQ

```python
index.train(vectors)
```

### Query Phase

- Uses trained structure
- Happens per request

```python
index.search(query, k)
```

📌 **Flat & HNSW do NOT require training**

---

## 5️⃣ Memory vs Disk Storage

### In-Memory Index

- Fastest
- RAM intensive
- Common in production

### Disk-Based / Persisted Index

- Load at startup
- Snapshot backups
- Used for durability

```python
faiss.write_index(index, "index.faiss")
faiss.read_index("index.faiss")
```

📌 **FAISS ≠ database**  
Persistence must be managed explicitly

---

## 6️⃣ Vector Persistence & Metadata (Production Reality 🏭)

### What FAISS Stores

- Vectors
- Internal structure
- Vector IDs

### What FAISS Does NOT Store

- ❌ Text
- ❌ Metadata
- ❌ Filters

### Common Architecture

```
FAISS (vector → ID)
Postgres / Mongo (ID → metadata)
```

📌 **Interviewers love this answer.**

---

## 7️⃣ Hands-On: FAISS from Scratch 🛠️

### Step 1️⃣ Create Dummy Embeddings

```python
import numpy as np

vectors = np.random.rand(1000, 384).astype("float32")
```

### Step 2️⃣ Create Index

```python
import faiss

index = faiss.IndexFlatIP(384)
```

📌 **IP = inner product** (use with normalized vectors)

### Step 3️⃣ Add Vectors

```python
index.add(vectors)
```

### Step 4️⃣ Search Top-K

```python
query = np.random.rand(1, 384).astype("float32")
D, I = index.search(query, k=5)
```

- `D` → similarity scores
- `I` → vector IDs

### Step 5️⃣ Save & Load Index

```python
faiss.write_index(index, "index.faiss")
index = faiss.read_index("index.faiss")
```

---

## 8️⃣ Common Mistakes (Learn These Early ⚠️)

- ❌ Forgetting normalization
- ❌ Using Flat index for millions of vectors
- ❌ Wrong distance metric
- ❌ Not tuning nprobe / efSearch
- ❌ Assuming FAISS handles metadata

---

## 9️⃣ Interview Questions You WILL Be Asked 🎤

### Fundamentals

**Why not brute-force similarity search?**  
→ O(N×D) complexity

**Flat vs IVF vs HNSW?**  
→ Accuracy vs speed vs memory

### Design

**How would you search 100M vectors?**  
→ IVF or HNSW + sharding

**How do you persist FAISS indexes?**  
→ Save to disk, reload at startup

### Tradeoffs

**When would you choose IVF over HNSW?**  
→ Lower memory, batch search

**What happens if vectors aren't normalized?**  
→ Similarity becomes meaningless

---

## 🧠 Final Summary (Memorize This)

**FAISS accelerates similarity search by reducing the number of comparisons.**

- **Flat** → compares everything
- **IVF** → compares cluster subset
- **HNSW** → walks graph intelligently

---

## ✅ Outcome Achieved

- ✔ You understand ANN indexing
- ✔ You can design scalable vector search
- ✔ You can explain FAISS confidently in interviews