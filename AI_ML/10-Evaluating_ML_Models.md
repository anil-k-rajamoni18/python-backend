# 📘 Session Notes: Evaluating ML Models & Search Systems

**(ML + RAG + Search + Vector DB + Hybrid Search)**

---

## 🧠 1️⃣ How to Evaluate ML Models (In-depth)

Model evaluation depends on the type of ML problem.

### 🎯 A. Evaluation for Classification Models

Used for spam detection, sentiment analysis, fraud detection, etc.

#### Metrics

#### 1️⃣ Accuracy

**% of correct predictions**

⚠️ Not reliable when data is imbalanced

**Example:**
```
If only 1% transactions are fraud → model predicts ALL as non-fraud → 99% accuracy but useless.
```

#### 2️⃣ Precision

**"How many predicted positives are actually positive?"**

**Formula:**

```
Precision = TP / (TP + FP)
```

Used when cost of false positives is high.

🛠 **Example:** You don't want to wrongly ban legitimate user accounts.

#### 3️⃣ Recall (Sensitivity)

**"How many true positives did we capture?"**

**Formula:**

```
Recall = TP / (TP + FN)
```

Used when missing a positive is costly.

🛠 **Example:** Missing a cancer case is dangerous → need high recall.

#### 4️⃣ F1 Score

**Harmonic mean of precision and recall**

Balances both

**Formula:**

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

#### 5️⃣ ROC-AUC

- Measures ranking quality
- AUC = probability a positive ranks higher than a negative

**Best for:**

- ✔ Binary classification
- ✔ When prediction scores are available

### 📈 B. Evaluation for Regression Models

Used for price prediction, forecasting, ratings.

#### Metrics:

**1️⃣ MAE (Mean Absolute Error)**  
Average absolute difference.

**2️⃣ MSE (Mean Squared Error)**  
Penalizes bigger errors.

**3️⃣ RMSE**  
Square root of MSE.

**4️⃣ R² Score**  
Explains variance captured by the model.

### ❗C. Evaluation for Clustering Models

Used for grouping users, topics, segments.

#### Metrics:

- Silhouette Score
- Davies–Bouldin Index
- Calinski–Harabasz Score

### 🚀 D. Evaluation for Embedding Models

*(Important for RAG & Semantic Search)*

#### Metrics:

- Cosine similarity ranking
- Triplet loss evaluation
- MTEB benchmark
- STS (Semantic Text Similarity) score

---

## 🔍 2️⃣ How to Evaluate Search Quality (Hybrid + Semantic)

Search systems exist in 3 forms:

1. **1️⃣ Keyword search** (BM25)
2. **2️⃣ Semantic search** (Embeddings)
3. **3️⃣ Hybrid search** (BM25 + Embeddings)

Evaluation metrics focus on retrieval quality.

### 🎯 A. Search Evaluation Metrics

#### 1️⃣ Recall@K

**"How many relevant documents appear in the top K results?"**

**Example:**
```
Out of 10 relevant documents, top-5 returned 3 →
Recall@5 = 30%
```

#### 2️⃣ Precision@K

**"How many of the top K results are correct?"**

**Example:**
```
Top 5 → 3 are relevant →
Precision@5 = 60%
```

#### 3️⃣ MRR (Mean Reciprocal Rank)

Measures ranking of the first correct result.

**Example:**
```
If first relevant result is in position 3 →
MRR = 1/3
```

Used for Q&A systems.

#### 4️⃣ nDCG (Normalized Discounted Cumulative Gain)

Measures how well ranked results match graded relevance.

**Used in:**

- ✔ Google search
- ✔ Recommendation engines
- ✔ Ecommerce ranking

#### 5️⃣ Human Evaluation (Gold Standard)

Ask SMEs to label:

- Relevance
- Context fit
- Completeness
- Accuracy

Used for RAG-based search systems.

### 🧪 B. Example: Evaluating Semantic Search

**User Query:**
```
"How do I set up automatic backups in AWS S3?"
```

**Retrieve documents:**

| Rank | Document | Human Relevance (0–3) |
|------|----------|----------------------|
| 1 | S3 Pricing | 0 |
| 2 | S3 Replication | 2 |
| 3 | Backup automation guide | 3 |
| 4 | CloudFormation intro | 1 |

Using nDCG, MRR, Precision@K → evaluate.

---

## 🔧 3️⃣ How to Improve Search Systems (Hybrid + Semantic)

Search quality depends on:

- The query
- The embeddings
- The vector DB
- The ranking model
- Metadata filtering
- Hybrid scoring

Below are in-depth techniques.

### 🚀 A. Techniques to Improve Semantic Search

#### 1️⃣ Better Embedding Model

**Replace:**

```
text-embedding-ada-002
```

**with**

```
text-embedding-3-large
```

**or**

```
bge-large
```

**or**

```
nomic-embed-text
```

Improves semantic matching.

#### 2️⃣ Chunking Optimization

**Use:**

- Recursive chunking
- Overlapping windows
- Semantic chunking

Chunk size affects answer quality.

#### 3️⃣ Metadata Filtering

**Add metadata such as:**

- Source type
- Tags
- Page number
- Author
- Topic

**Use vector DB filters:**

```python
where={"category": "finance"}
```

#### 4️⃣ Hybrid Search (BM25 + Embeddings)

**Best of both worlds:**

- BM25 for exact keywords
- Embeddings for semantics

**Score combination:**

```
final_score = α * embedding_score + (1-α) * bm25_score
```

#### 5️⃣ Reranking (Re-Ranker Models)

**Use:**

- Cohere ReRank
- bge-reranker
- LLaMA-3-8B Instruct as re-ranker

These models re-rank top-K documents using LLM reasoning.

#### 6️⃣ Query Expansion

Auto-rewrite user queries:

```
"cloud cost optimization"
→ "reduce cloud bills, AWS savings, cost control strategies"
```

#### 7️⃣ Use Query Rewriting LLM

Rewrite queries to be:

- more complete
- more specific
- more contextual

**Example:**

```
User: "How to secure login?"

Rewritten:
"best practices for securing user authentication on web apps"
```

#### 8️⃣ Use Multiple Embeddings (Ensemble)

**Combine:**

- Dense embeddings
- Sparse embeddings
- Cross-encoders

### 🎯 B. Example: Improving Hybrid Search

**User Query:**
```
"Reset password flow for enterprise account"
```

Initial results are weak.

**Improvements:**

1. Use domain-specific embedding model
2. Add keywords like "password reset", "enterprise SSO", "identity management"
3. Multi-vector retrieval
4. Reranker model

**Outcome:**  
Top results become highly relevant.

---

## 🚀 Full Workflow: Build + Evaluate + Improve Search

### Step 1: Ingest Documents

→ chunk → embed → store in vector DB

### Step 2: Implement Basic Search

```python
embedding_simmilarity(query, docs)
```

### Step 3: Evaluate

**Use:**

- Precision@5
- Recall@5
- MRR

### Step 4: Improve

- tune embeddings
- use hybrid search
- add metadata filtering
- re-rank results

### Step 5: Validate with Human Experts

SMEs check relevance.

---

## 🎓 Summary Table

| Topic | What You Measure | Tools |
|-------|------------------|-------|
| ML models | Accuracy, F1, ROC-AUC | sklearn, huggingface |
| Semantic search | Recall@K, nDCG | Ragas, custom scripts |
| Hybrid search | combined score | BM25 + embeddings |
| Improvement | embeddings, chunking, reranking | re-rankers, hybrid scoring |