# Embeddings & Semantic Search Guide

## 🧠 0. Mental Model Before We Begin (Very Important)

**Embeddings convert human language into geometry.**  
Once text becomes vectors in space, search becomes math, not NLP.

If you remember only one thing today, remember this:

> 🔑 **Semantic search works because meaning → distance.**

---

## 1️⃣ What Are Embeddings? (WHY first)

### Real-World Analogy 🗺️

Imagine a Google Maps–like space:

- Restaurants are close to restaurants
- Schools are near schools
- Airports are far from hospitals

Now replace places with sentences.

➡️ **Embeddings place text into a high-dimensional semantic map**

### Formal Definition (Interview-Safe)

An **embedding** is a fixed-length dense numerical vector that captures the semantic meaning of text.

**Example:**
```
"I love machine learning" → [0.12, -0.87, 1.02, ...]
```

### Why We Need Embeddings

**Traditional keyword search:**
- ❌ "car" ≠ "automobile"
- ❌ "refund policy" ≠ "return rules"

**Embeddings:**
- ✅ Understand meaning, not words
- ✅ Handle paraphrases
- ✅ Work even when words don't overlap

📌 This is the foundation of semantic search, RAG, chatbots, recommendation systems

---

## 2️⃣ Dense vs Sparse Representations

### Sparse Representations (Old World 🧓)

**Examples:**
- Bag of Words
- TF-IDF
- BM25

**Characteristics:**
- Huge vectors (vocab size)
- Mostly zeros
- Exact word matching

**Example:**
```
"I like cats" → [0,0,1,0,0,1,0...]
```

**Pros & Cons:**
- ✅ Fast
- ❌ No semantics
- ❌ Vocabulary explosion

### Dense Representations (Modern World 🚀)

**Examples:**
- Word2Vec
- Sentence-BERT
- E5

**Characteristics:**
- Small fixed size (e.g., 384, 768)
- Every value meaningful
- Semantic understanding

**Example:**
```
"I like cats" → [0.23, -0.44, 0.91, ...]
```

### Interview Insight ⚡

**BM25 is lexical; embeddings are semantic.**  
Best systems combine both (Hybrid Search).

---

## 3️⃣ Word Embeddings vs Sentence Embeddings

### Word Embeddings (Word2Vec, GloVe)

Each word has a vector.

**Example:**
```
king - man + woman ≈ queen
```

**Problems:**
- ❌ No context
- ❌ Polysemy fails (bank = river vs money)

### Sentence Embeddings (Modern Standard ✅)

Each sentence / paragraph / document has one vector.

**Example:**
```
"I went to the bank to deposit money"
```

➡️ Model understands context

### Why Sentence Embeddings Win (Production Reality)

- Search queries are sentences
- Docs are paragraphs
- Context > vocabulary

📌 In interviews: always prefer sentence embeddings unless explicitly asked

---

## 4️⃣ Bi-Encoders vs Cross-Encoders (🔥 VERY IMPORTANT)

### Bi-Encoder (Most Search Systems)

```
Query → Encoder → Vector
Doc   → Encoder → Vector
Similarity(query, doc)
```

**Pros & Cons:**
- ✅ Precompute document embeddings
- ✅ Fast (millions of docs)
- ❌ Slightly less accurate

**Used in:**
- FAISS
- Pinecone
- Weaviate
- Milvus

### Cross-Encoder (Accuracy Monster 🐉)

```
[Query + Document] → Transformer → Score
```

**Pros & Cons:**
- ✅ Extremely accurate
- ❌ Very slow
- ❌ No precomputation

**Used in:**
- Reranking (top-k results)
- Legal / medical search
- Final relevance scoring

### Golden Interview Answer 🏆

> "We retrieve candidates using a bi-encoder and rerank using a cross-encoder."

---

## 5️⃣ Similarity Metrics (Math That Actually Matters)

### 🔹 Cosine Similarity (Most Common)

Measures angle, not magnitude.

```
cos(A, B) = (A · B) / (||A|| ||B||)
```

**Range:**
- 1.0 → identical meaning
- 0.0 → unrelated
- -1.0 → opposite

**Pros:**
- ✅ Length-invariant
- ✅ Best for embeddings

### 🔹 Dot Product

```
A · B
```

- Faster
- Sensitive to vector magnitude

📌 Often used after normalization

### 🔹 Euclidean Distance

```
||A - B||
```

- Measures raw distance
- Less common for text embeddings

### Interview Tip 🎯

**If embeddings are normalized → cosine similarity = dot product**

---

## 6️⃣ Embedding Normalization (Small Step, Big Impact)

### What is it?

Scaling vectors to unit length:
```
||v|| = 1
```

### Why normalize?

- Removes length bias
- Makes similarity comparable
- Stabilizes ANN search

📌 Many modern models already output normalized vectors  
📌 Always verify in production

---

## 7️⃣ Popular Embedding Models (What to Use & WHY)

### 🔹 Sentence-BERT (SBERT)

- Fine-tuned BERT for sentence similarity
- Strong semantic understanding
- Slightly heavier

**Use when:**
- Accuracy > latency

### 🔹 MiniLM

- Smaller, faster
- Very popular in production
- Excellent tradeoff

**Use when:**
- Latency matters
- Large-scale retrieval

### 🔹 E5 (Embeddings for Everything 🔥)

- Designed for search
- Query & document prefixes:

```python
"query: how to reset password"
"passage: click on forgot password"
```

**Use when:**
- Building search / RAG systems
- You want SOTA retrieval

📌 **Interviewers LOVE E5**

---

## 8️⃣ Hands-On (Minimal but Meaningful 🛠️)

### Step 1: Load Model

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
```

### Step 2: Generate Embeddings

```python
sentences = [
    "How to reset my password?",
    "Steps to change account credentials",
    "Best pizza places in Hyderabad"
]

embeddings = model.encode(sentences, normalize_embeddings=True)
```

### Step 3: Cosine Similarity

```python
from sklearn.metrics.pairwise import cosine_similarity

cosine_similarity([embeddings[0]], [embeddings[1]])
cosine_similarity([embeddings[0]], [embeddings[2]])
```

**Expected:**
- High similarity → password sentences
- Low similarity → pizza sentence

---

## 9️⃣ Why Semantic Search Works (Final Mental Model 🎯)

1. Language → vectors
2. Meaning → geometry
3. Similar meaning → nearby vectors
4. Search → nearest neighbors

- ❌ No keywords
- ✅ No synonyms list
- ✅ Pure math

---

## 🔟 Common Mistakes (Learn from Others' Pain 😅)

- ❌ Using word embeddings for document search
- ❌ Forgetting normalization
- ❌ Using cross-encoder for full corpus
- ❌ Assuming higher dimension = better
- ❌ Ignoring hybrid (BM25 + embeddings)

---

## 🧠 Interview Follow-Up Questions You WILL Get

1. Why cosine over Euclidean?
2. Bi-encoder vs cross-encoder tradeoffs?
3. How embeddings differ from TF-IDF?
4. How do you evaluate embedding quality?
5. How does normalization affect ANN indexes?

👉 You should now confidently answer all of them.

---

## ✅ Outcome Achieved

- ✔ You understand embeddings intuitively
- ✔ You can explain semantic search clearly
- ✔ You are ready for senior ML / search interviews