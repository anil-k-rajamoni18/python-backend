# 🗃️ Session Notes: Chunking & Document Processing for RAG

**Chunking & Document Processing is the heart of a RAG system.**  
Even if you use the best LLM + vector database, **bad chunking = bad retrieval → bad answers.**

---

## 🎯 Why Chunking Matters

LLMs can only ingest limited tokens (context window).  
So we must break large documents into smaller pieces that are:

- semantically meaningful 🧠
- dense with information 📑
- easily retrievable 🔍
- properly indexed in a vector DB 📦

**Good chunking leads to:**

- ✨ Higher retrieval accuracy
- ✨ Better grounding
- ✨ Less hallucination
- ✨ Efficient search
- ✨ Faster inference

---

## 1️⃣ What Is Chunking?

**Chunking** = splitting long text into smaller parts (chunks) that can be embedded and stored in a vector DB.

Each chunk typically has:

- text content
- metadata (page no., heading, source, timestamp)
- unique ID
- embedding

---

## 2️⃣ Chunk Size Basics 📏

**Typical ranges:**

- **Small chunks:** 150–300 tokens  
  ✓ better for short Q&A

- **Medium chunks:** 300–600 tokens  
  ✓ ideal for documentation

- **Large chunks:** 600–1200 tokens  
  ✓ better for narrative content

### 🔧 Choose chunk size based on:

- Type of text
- Granularity required
- Query type
- Embedding model

---

## 3️⃣ Chunking Strategies (Core of RAG)

Let's cover the most important chunking methods.

### 🧩 3.1 Recursive Chunking

*(also called Recursive Character Text Splitter)*

#### 📘 What is Recursive Chunking?

It splits text based on priority breakpoints:

- Paragraphs
- Newlines
- Sentences
- Words
- Characters

It tries larger boundaries first, and if chunk too large → splits again recursively.

**Example:**
```
Document
 ├─ Paragraph
 │   ├─ Sentence 1
 │   ├─ Sentence 2
 │   └─ Sentence 3
```

#### 👍 Why It's Useful?

- Maintains structure
- Avoids splitting mid-sentence
- Ideal for general text

#### 🔧 Typical Tools:

- LangChain RecursiveCharacterTextSplitter
- LlamaIndex NodeSplitter

### 🧠 3.2 Semantic Chunking

*(advanced + best for knowledge-heavy documents)*

#### 📘 What is Semantic Chunking?

Uses an LLM or embedding model to determine natural boundaries based on meaning, not size.

**How it works:**

1. Compute embeddings for sentences/paragraphs.
2. Group similar ones together.
3. Produce semantically coherent chunks.

#### 👍 Why It's Powerful?

- Better retrieval quality
- More aligned with real topics
- Higher grounding
- Best for technical docs, PDFs, research papers

#### 🔧 Tools:

- OpenAI semantic chunker
- LangChain SemanticChunker
- custom embedding-based clustering

### 🏷️ 3.3 Heading-Aware Chunking

Chunk based on:

- **H1** → major sections
- **H2** → sub-sections
- **H3** → paragraphs

**Best for:**

- Markdown
- Technical docs
- Manuals
- API docs

**Benefits:**

- Chunks remain context-aware
- Improves search relevance

### 🧩 3.4 Fixed-Size Chunking

Splits into equal-sized parts (e.g., 500 tokens each).

**Pros:**

- Simple
- Fast
- Good for clean text

**Cons:**

- Breaks meaning
- Poor accuracy
- Rarely used alone — often paired with overlap.

### 🔄 Overlapping Chunks

**Chunk overlap** = repeating some text between chunks.

**Example:**

```
Chunk size = 300 tokens
Overlap = 50 tokens
```

**Why use overlap?**

- ✔ Keeps context consistent
- ✔ Ensures queries match boundaries
- ✔ Improves retriever accuracy

---

## 📄 4️⃣ PDF Parsing – Real-Life Challenge

PDFs are messy. **Problems include:**

- multi-column layouts
- broken sentences
- tables
- headers/footers
- images
- OCR issues

**Tools for PDF parsing:**

- **pypdf** — simple extraction
- **pdfminer.six** — handles complex layouts
- **PyMuPDF (fitz)** — best accuracy
- **Unstructured.io** — premium quality
- **Textract** — OCR+PDF
- **Tesseract** — required for scanned PDFs

### 📐 PDF Parsing Workflow

```
1. Load PDF
   ↓ Extract text + metadata.

2. Clean text
   ↓ Fix spacing
   ↓ Remove headers/footers
   ↓ Remove page numbers

3. Chunk text
   ↓ Semantic or recursive.

4. Embed + store
   ↓ Send to vector DB.
```

---

## 🧹 5️⃣ Cleaning & Preprocessing

Before chunking, **always clean text.**

### 🔧 What to clean?

- Extra spaces
- Newlines
- Unicode artifacts
- Page numbers
- Footer URLs
- Table of contents
- Trailing hyphens in wrapped words
- OCR noise

**Tools:**

- Regex
- spaCy
- LangChain cleaners
- unstructured

---

## 📊 6️⃣ Example: Chunking Pipeline (RAG)

```
PDF -> Extract Text -> Clean -> Chunk -> Embed -> Store -> Query -> RAG -> Answer
```

---

## 🛠️ 7️⃣ Real-Time Hands-On Example

### Example 1: Recursive Chunking with LangChain

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = open("doc.txt").read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = splitter.split_text(text)
len(chunks)
```

### Example 2: Semantic Chunking

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

embedder = OpenAIEmbeddings(model="text-embedding-3-small")
chunker = SemanticChunker(embeddings=embedder)

chunks = chunker.split_text(text)
```

### Example 3: PDF Parsing with PyMuPDF

```python
import fitz

doc = fitz.open("sample.pdf")
text = ""

for page in doc:
    text += page.get_text()
```

### Example 4: Cleaning Text

```python
import re

def clean(t):
    t = re.sub(r'\n+', '\n', t)
    t = re.sub(r'-\n', '', t)    
    t = re.sub(r'\s+', ' ', t)
    return t.strip()
```

---

## 🧠 8️⃣ Best Practices

- ✔ Use semantic chunking when possible
- ✔ Use recursion for messy docs
- ✔ Always clean before chunking
- ✔ Keep chunk overlap between 30–60 tokens
- ✔ Preserve metadata (page #, section)
- ✔ For PDFs → use PyMuPDF or Unstructured
- ✔ Don't make chunks too small
- ✔ Don't mix multiple documents in one chunk

---

## 🎯 9️⃣ What Not To Do

- ❌ Don't split arbitrarily
- ❌ Don't store full documents in 1 chunk
- ❌ Don't ignore headings
- ❌ Don't skip cleaning
- ❌ Don't use too large chunks (>1,500 tokens)
- ❌ Don't remove semantic context

---

## 🔟 Summary Table

| Concept | Purpose | Best Use |
|---------|---------|----------|
| Recursive Chunking | Structure-aware splitting | Blogs, books, PDFs |
| Semantic Chunking | Meaning-aware splitting | Technical docs, research |
| PDF Parsing | Extract text from complex PDFs | Enterprise docs |
| Cleaning | Remove noise | All ingestion pipelines |