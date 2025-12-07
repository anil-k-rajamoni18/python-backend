# 🔥 REAL-TIME SCENARIO–BASED INTERVIEW QUESTIONS (Embeddings + Vector DBs)

---

## ✅ 1️⃣ Scenario: Document Search Engine Performing Poorly

### Question:
You built a semantic search engine for your company's internal documents. Users say the system often returns irrelevant results. What steps would you take to troubleshoot and improve retrieval quality?

### Expected Answer:

- Check chunking strategy (overlaps, sizes)
- Re-generate embeddings using a better model
- Normalize vectors before indexing
- Ensure correct similarity metric (cosine vs L2)
- Use reranking model on top-k results
- Validate the data indexing pipeline for missing chunks
- Add metadata filtering

---

## ✅ 2️⃣ Scenario: RAG System Hallucinating

### Question:
Your RAG chatbot still hallucinates even after retrieving relevant chunks from the vector DB. What could be the reasons?

### Expected Answer:

- Retrieved chunks are semantically similar but not factual
- Chunk size too small → incomplete context
- LLM instruction not forcing grounded answers
- Retrieval returns too many/few chunks
- Embeddings are outdated after document updates
- Missing metadata filtering (e.g., wrong department, old docs)

---

## ✅ 3️⃣ Scenario: Vector DB Cost Optimization

### Question:
Company wants to reduce Pinecone costs. What are practical ways to optimize?

### Expected Answer:

- Reduce embedding dimensions (use MiniLM instead of large models)
- Use metadata filters before similarity search
- Limit top_k results
- Use hybrid indexing: part in Pinecone, part in local FAISS
- Compress vectors (quantization)
- Periodically delete outdated embeddings

---

## ✅ 4️⃣ Scenario: Multilingual Knowledge Base Failing Searches

### Question:
Your company supports international users (English, French, Hindi). Semantic search works in English but fails badly in other languages. What do you do?

### Expected Answer:

- Switch to multilingual embedding model (LaBSE, mUSE, MiniLM multilingual)
- Check tokenizer compatibility
- Separate vector DB per language or add metadata for filtering
- Normalize unicode text before embedding
- Add translation pipeline only if quality is acceptable

---

## ✅ 5️⃣ Scenario: FAISS Memory Running Out

### Question:
Your FAISS index crashes due to memory issues when indexing millions of documents. What is your solution?

### Expected Answer:

- Use FAISS IVF or HNSW indexes for approximate search
- Store vectors on disk, not memory
- Enable FAISS GPU indexes
- Switch to external DB like Qdrant/Pinecone
- Use quantized vectors (PQ, OPQ) to reduce memory footprint

---

## ✅ 6️⃣ Scenario: Wrong Results After Updating Documents

### Question:
Your document search engine gives outdated results after updating documents. Why?

### Expected Answer:

- Old embeddings not re-generated
- Index not refreshed
- Deleted documents still exist in vector DB
- Metadata not consistent with updated content
- ID mismatches while adding new vectors

---

## ✅ 7️⃣ Scenario: Query Expansion Needed

### Question:
Users ask vague queries like "fix laptop" but your vector DB retrieves poor results. How can you solve this?

### Expected Answer:

- Use LLM to rewrite/expand user queries
- Apply multiple embedding representations (hybrid search)
- Store synonyms or domain taxonomy
- Add BM25 keyword search + embedding search → hybrid retrieval

---

## ✅ 8️⃣ Scenario: Combining Multiple Data Sources

### Question:
Your RAG system needs to index PDFs, Word docs, meeting transcripts, and SQL data. What's the best approach?

### Expected Answer:

- Convert all documents to text
- Chunk them using appropriate strategies per type
- Add metadata (source, page, department)
- Store in one vector DB but use metadata filters
- Convert SQL rows into natural language before embedding

---

# 🧪 HANDS-ON LLM + VECTOR DB EXERCISES (Practical & Interview-Ready)

---

## ⭐ Exercise 1 — Build a Simple Embedding Search (FAISS)

### Task:
Given 10 text sentences, embed them, store in FAISS, and retrieve top-3 for a query.

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

data = [
    "Python is a great programming language",
    "Cats are beautiful pets",
    "Dogs are loyal animals",
    "Machine learning is a subset of AI",
    "Transformers are deep learning architectures",
    "I love Indian food",
    "Neural networks learn patterns",
    "Pizza is delicious"
]

# Embeddings
emb = model.encode(data).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

# Query
query = model.encode(["Explain deep learning"]).astype("float32")
dist, idx = index.search(query, 3)

for i in idx[0]:
    print(data[i])
```

---

## ⭐ Exercise 2 — Create a ChromaDB Semantic Search

```python
from chromadb import Client
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
db = Client()

collection = db.create_collection(name="my_docs")

texts = [
    "The Eiffel tower is in Paris",
    "Statue of Liberty is in New York",
    "The Taj Mahal is in India"
]

embeddings = model.encode(texts).tolist()

for i, t in enumerate(texts):
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings[i]],
        metadatas=[{"source": "wiki"}]
    )

q = model.encode("Where is Taj located?").tolist()

result = collection.query(query_embeddings=q, n_results=1)
print(result)
```

---

## ⭐ Exercise 3 — Build Chunking Logic

### Task:
Write code to:
- Split a long text into chunks
- Use overlap of 30%
- Store chunks + embeddings

```python
def chunk_text(text, chunk_size=200, overlap=60):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
```

---

## ⭐ Exercise 4 — Evaluate Cosine Similarity Manually

```python
from numpy import dot
from numpy.linalg import norm

def cosine(a, b):
    return dot(a, b) / (norm(a) * norm(b))
```

Compute similarity between:
- "dog"
- "cat"
- "pizza"

### 👉 Show that dog-cat is highest similarity.

---

## ⭐ Exercise 5 — Create a Mini "Ask Your Documents" Search Engine

### Steps:

1. Load a long article
2. Chunk it
3. Embed chunks
4. Store in ChromaDB
5. Ask a question
6. Retrieve top-k chunks
7. Print results

**This forms the foundation of a full RAG pipeline.**

---

## ⭐ Exercise 6 — Compare Different Chunk Sizes

### Task:
Chunk the same document with 100, 300, and 500 characters

**Measure:**
- retrieval relevance
- index size
- accuracy of returned chunks

**Observe:**
- Small chunks → more accurate retrieval but fragmented context
- Large chunks → lose precision

---

## ⭐ Exercise 7 — Detect Which Vector DB to Use

Given 3 test documents and a query, store embeddings in:
- FAISS
- Chroma

**Compare:**
- Speed
- Ease of use
- Result differences

---

## ⭐ Exercise 8 — Convert SQL Table into Natural Language Embeddings

**Given a table:**

| id | name | salary | location |
|----|------|--------|----------|
| 1 | John | 50k | US |
| 2 | Priya | 80k | India |

**Convert to:**
```
"Employee John from US earns 50k."
```

Then embed and store.

**This is real-world RAG for structured data.**