# Keyword Search & BM25 Guide

## 🧠 0. Core Mental Model (Set This First)

**Keyword search answers:** "Does this document contain the terms I care about?"  
**Semantic search answers:** "Does this document mean what I want?"

**Great search systems use both.**

---

## 1️⃣ Why Keyword Search Still Matters (Even in 2025)

### Reality Check 🚨

**Embeddings:**
- ❌ Struggle with numbers, IDs, codes
- ❌ Can hallucinate relevance
- ❌ May miss exact matches

**Keyword search:**
- ✅ Exact term matching
- ✅ Deterministic
- ✅ Interpretable

📌 Regulated, enterprise, and legal systems rely heavily on keywords.

### Real-World Examples 🏭

- Error codes: `ORA-12514`
- Part numbers: `AX-239-B`
- Legal clauses: "Section 54F"
- Names, SKUs, phone numbers

➡️ **Embeddings alone fail badly here.**

---

## 2️⃣ TF-IDF vs BM25 (Evolution of Keyword Scoring)

### 🔹 TF-IDF (Old but Important)

#### What It Measures

- **TF (Term Frequency):** How often term appears
- **IDF (Inverse Document Frequency):** How rare the term is

**Basic idea:**  
Important words = frequent in document, rare in corpus

#### Why TF-IDF Fails at Scale ❌

- Overweights long documents
- Linear TF scaling (bad)
- No length normalization

---

### 🔹 BM25 (Modern Keyword Scoring ⭐)

#### Key Improvements

- Saturated TF (diminishing returns)
- Document length normalization
- Tunable parameters

**Simplified intuition:**  
First occurrence of a keyword matters more than the 10th.

#### BM25 Core Parameters

| Parameter | Meaning               |
|-----------|-----------------------|
| k1        | TF saturation         |
| b         | Length normalization  |

**Typical values:**
- k1 ≈ 1.2–2.0
- b ≈ 0.75

📌 **Interviewers love when you mention these.**

---

## 3️⃣ Tokenization (Where Search Often Breaks ⚠️)

### What Is Tokenization?

Breaking text into searchable units (tokens).

**Example:**
```
"Error-404_not_found" →
["error", "404", "not", "found"]
```

### Why Tokenization Matters

Wrong tokenizer → wrong results.

**Examples:**
- Code search
- Hyphenated words
- CamelCase
- Indian names (multi-part)

📌 **Most "BM25 bugs" are tokenization bugs.**

---

## 4️⃣ Inverted Index (The Backbone of Keyword Search)

### Mental Model 📚

Like a book index:
```
"python" → [doc1, doc7, doc42]
```

### Why It's Powerful

- Query time ∝ number of matching docs
- Extremely fast
- Scales to billions of documents

### Structure

```
Term → Posting list (docID, frequency)
```

📌 **Embeddings cannot replace this efficiency for exact terms.**

---

## 5️⃣ Precision vs Recall (Very Interview-Critical ⚖️)

### Precision

**Of retrieved results, how many are relevant?**

**High precision:**
- Legal search
- Compliance
- Debugging

### Recall

**Of all relevant results, how many did we retrieve?**

**High recall:**
- Discovery search
- Recommendation
- Q&A systems

### Keyword vs Semantic

| System     | Precision | Recall |
|------------|-----------|--------|
| BM25       | High      | Medium |
| Embeddings | Medium    | High   |
| Hybrid     | High      | High   |

📌 **Hybrid search exists because of this table.**

---

## 6️⃣ Hands-On: BM25 in Python 🛠️

### Step 1️⃣ Documents

```python
docs = [
    "How to reset my password",
    "Password reset steps for user account",
    "Pizza delivery services near me"
]
```

### Step 2️⃣ Tokenize

```python
tokenized = [doc.lower().split() for doc in docs]
```

📌 Real systems use analyzers (stemming, stopwords).

### Step 3️⃣ BM25 Index

```python
from rank_bm25 import BM25Okapi

bm25 = BM25Okapi(tokenized)
```

### Step 4️⃣ Query

```python
query = "password reset"
scores = bm25.get_scores(query.split())
```

### Step 5️⃣ Analyze Results

- Exact keyword matches score highest
- Semantic similarity not considered

---

## 7️⃣ BM25 vs Semantic Search (Failure Analysis 🔍)

### Query: "How can I change my login credentials?"

**BM25 Fails ❌**
- No word overlap with "password reset"

**Embeddings Win ✅**
- Captures paraphrase

---

### Query: "ORA-12514 database error"

**BM25 Wins ✅**
- Exact term matching

**Embeddings Fail ❌**
- Treats as random tokens

📌 **This is the strongest argument for hybrid search.**

---

## 8️⃣ Elasticsearch (Industry Standard 🏗️)

### What Elasticsearch Adds

- Inverted index
- BM25 scoring
- Tokenizers & analyzers
- Filters & aggregations

📌 **Embeddings can be added, not replaced.**

### Typical ES Flow

```
Document → Analyzer → Inverted Index → BM25
```

---

## 9️⃣ Common Mistakes (Real Production Issues ⚠️)

- ❌ Relying only on embeddings
- ❌ Ignoring tokenizer behavior
- ❌ No stopword handling
- ❌ Misinterpreting BM25 scores
- ❌ Confusing recall with precision

---

## 🔟 Interview Questions You WILL Get 🎤

### Fundamentals

**TF-IDF vs BM25?**  
→ BM25 handles TF saturation + length normalization

**Why keyword search still relevant?**  
→ Exact matches, determinism, compliance

### System Design

**When does BM25 beat embeddings?**  
→ IDs, codes, legal text

**How does inverted index work?**  
→ Term → posting lists

### Hybrid Search

**Why combine BM25 + embeddings?**  
→ Precision + recall

**How do you merge results?**  
→ Score normalization + reranking

---

## 🧠 Final Mental Summary (Memorize This)

**Keyword search is about certainty.**  
**Semantic search is about meaning.**  
**Hybrid search is about reality.**

---

## ✅ Outcome Achieved

- ✔ You understand BM25 deeply
- ✔ You can explain inverted indexes
- ✔ You can justify hybrid architectures