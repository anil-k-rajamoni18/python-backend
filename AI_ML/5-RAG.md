# 🚀 Session Notes: Retrieval-Augmented Generation (RAG)

---

## 🧠 1. What is RAG?

**RAG (Retrieval-Augmented Generation)** is an AI technique that combines:

- **Retrieval** → fetching relevant information from external sources
- **Generation** → using an LLM to produce final user-facing answers

### In simple words:
👉 **LLM + Knowledge Base = RAG**

It allows LLMs to use fresh, domain-specific, verified information instead of relying only on what they were trained on.

### 🔥 Why RAG?

- Reduces hallucinations
- Provides up-to-date information
- Works with private enterprise data
- Improves accuracy & trustworthiness
- Cheaper than fine-tuning

---

## 🌍 2. Why Do We Need RAG?

LLMs (GPT, Llama, Claude) are static models — trained once, cannot access private data.

RAG solves key problems:

### ❌ Without RAG:

- Hallucinations
- No access to private documents
- No real-time data
- Weak accuracy in niche domains
- Hard to maintain model freshness

### ✔️ With RAG:

- Connects LLM → Your documents
- Accurate factual answers
- Supports enterprise workloads
- Easily updatable knowledge
- Cheaper than training or fine-tuning

### Example:
```
Bank LLM cannot answer "What is my EMI policy?"
But RAG can fetch the correct policy document and generate accurate answers.
```

---

## 🧩 3. Architecture of RAG (High-Level)

```
User Query → Embedding → Vector Search → Retrieve Docs →
LLM → Combines Docs + Reasoning → Final Answer
```

### Components:

1. User Query
2. Query Embedding Model
3. Vector Database (Pinecone, Chroma, Weaviate, Milvus)
4. Retriever
5. LLM (Generator)
6. Answer + Citations

---

## 🔎 4. RAG Pipeline (Deep Explanation)

### Step 1: 🔍 Document Ingestion

- Upload PDFs, text, CSV, Word files, websites
- Clean text
- Chunking (split into 200–500 token chunks)

### Step 2: 🧩 Vectorization

- Convert each chunk → vector embedding
- Store in vector DB with metadata:
  - doc_id
  - source
  - page
  - timestamp

### Step 3: 🔎 Retrieval

When user asks a question:

- Convert question → vector
- Search in DB → top-k relevant chunks

**Retrieval types:**

- Semantic search
- Hybrid search (vector + keyword)
- Reranking (Cross-Encoder)

### Step 4: 🤖 Generation

LLM receives:

- User query
- Retrieved chunks

**Example prompt:**

```
Use ONLY the provided documents to answer the question.  
If not found, say "Not available in knowledge base."

<context>
{retrieved_chunks}
</context>

Question: {user_query}
```

### Step 5: 📝 Response

LLM synthesizes answer + optionally citations.

---

## 🏛️ 5. RAG Components Explained

### 📘 A. Chunking Strategies

- Fixed-size (300 tokens)
- Semantic chunking (LLM-based breaks)
- Recursive chunking

**Best practice:**

200–400 token chunks → best balance.

### 🧬 B. Embeddings (Vector Representations)

**Common models:**

- OpenAI text-embedding-3-large
- BERT / SBERT
- InstructorXL
- Llama 3 embeddings

**Embedding size:** 384 → 3072 dimensions

### 🗄️ C. Vector Databases

**Popular Vector DBs:**

| DB | Type | Best Use Case |
|---|---|---|
| Pinecone | Cloud | Enterprise, scalable |
| ChromaDB | Local | Prototyping |
| Weaviate | Cloud/on-prem | Hybrid semantic search |
| Milvus | Open-source | Large-scale vector workloads |
| FAISS | Library | Local retrieval, offline |

### 🔎 D. Retrieval Methods

- Top-k semantic search
- MMR (diversity-enhanced)
- Hybrid search (BM25 + vectors)
- Cross-Encoder reranking (most accurate)

---

## 💡 6. Types of RAG

### 🎯 1. Basic RAG (Standard)

Chunk + Embed + Retrieve + Generate

### 🧠 2. Advanced RAG (Enhanced)

- Query rewriting
- Document reranking
- Multi-vector retrieval
- Metadata filtering
- Context pruning

### 💬 3. Conversational RAG

Maintains multi-turn history.

### 🔗 4. Agentic RAG (Next-gen)

LLM can:

- Browse URLs
- Query APIs
- Generate follow-up queries
- Decide which tool to use

---

## 🧪 7. RAG vs Fine-Tuning

| Feature | RAG | Fine-Tuning |
|---------|-----|-------------|
| Uses private data | ✔️ | ✔️ |
| Updatable | ✔️ instant | ❌ requires retraining |
| Cost | Low | High |
| Accuracy | Good | Best |
| Hallucination | Low | Medium |
| Works with large docs | ✔️ | ❌ |

**Best practice:**
➡️ Use RAG first, fine-tune only if necessary.

---

## 🚧 8. Challenges in RAG

- Poor chunking
- Wrong embedding model
- Retrieval mismatch
- Too large context → noisy LLM output
- Hallucination when retrieved docs are wrong

---

## 🛠️ 9. Best Practices

### 🔹 Retrieval

- Use hybrid search: BM25 + vectors
- Use rerankers like Cohere Rerank

### 🔹 Prompting

- Use strict instructions
- Add citations
- Restrict LLM to retrieved content

### 🔹 Evaluation

RAGAS metrics:

- hallucination score
- relevancy score
- grounding score

---

## 💼 10. Real-Time Hands-on Project

### 🏗️ Project: Build an Enterprise RAG Chatbot for Company Policies

### 📁 Step 1: Dataset

**Example documents:**

- HR policy PDF
- Leave policy
- Payroll guidelines
- WFH policy

Place them in `/data/policies/`.

### 🔍 Step 2: Document Loader (Python)

```python
from langchain.document_loaders import PyPDFLoader

docs = []
for file in ["hr.pdf", "leave.pdf", "payroll.pdf"]:
    loader = PyPDFLoader(f"./data/{file}")
    docs.extend(loader.load())
```

### 🧩 Step 3: Chunking

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80
)
chunks = splitter.split_documents(docs)
```

### 🧬 Step 4: Embedding + Vector DB

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
vector_db = FAISS.from_documents(chunks, embeddings)
```

### 🔎 Step 5: Retrieval

```python
retriever = vector_db.as_retriever(search_kwargs={"k": 4})
```

### 🤖 Step 6: RAG Chain (Generator)

```python
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

rag = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)
```

### 💬 Step 7: Query Example

```python
query = "How many casual leaves can an employee take per year?"
result = rag(query)

print(result["result"])
print(result["source_documents"])
```

### 🎉 Output (LLM Response)

```
"Employees can take 12 casual leaves per year as per the HR policy (Page 14)."
```

---

## 🧪 Extended Features You Can Add

- UI using Streamlit
- API using FastAPI
- RERANKING using Cohere Rerank
- CITATIONS in responses
- MEMORY for chat history

---

## 🎓 End of Session — Summary

- RAG connects LLMs to real knowledge
- Solves hallucination & outdated info
- Uses embeddings + vector DB
- Requires careful chunking, retrieval, prompting
- Project demonstrates full end-to-end RAG system