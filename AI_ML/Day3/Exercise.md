# 🔥 REAL-TIME SCENARIO–BASED INTERVIEW QUESTIONS (LLMs 101)

---

## 1️⃣ Scenario: Building a Customer Support Chatbot

### Question:
Your company wants to build a chatbot that answers customer FAQs using an LLM without storing any customer data. How would you design your system prompt and user prompt so the model always responds professionally and avoids hallucinating policy details?

### Expected Answer:

- System prompt: enforce tone, guardrails
- Include constraints:
  - "If unsure, say 'I don't have enough information'."
  - "Do not fabricate company policies."
- Few-shot examples to show proper responses
- Validate outputs (optionally) with rule-based checks

---

## 2️⃣ Scenario: Hallucinations in Product Descriptions

### Question:
Your LLM occasionally generates non-existent product features. How would you modify your prompt to reduce hallucinations?

### Expected Answer:

- Provide structured input → structured output
- Include a "don't make up information" rule
- Ask to quote only given context
- Add examples of acceptable vs unacceptable answers
- Enable self-checking:
  ```
  "Before final answer, re-evaluate if statements are factual."
  ```

---

## 3️⃣ Scenario: Multilingual Tokenization Problem

### Question:
Your application handles English + Hindi text. Users complain Hindi queries produce worse responses. What steps would you take to investigate?

### Expected Answer:

- Check tokenizer compatibility with Hindi
- Inspect embedding vector quality
- Use multilingual embedding models (e.g., sentence-transformers)
- Check for unseen tokens (rare subword tokens)
- Possibly retrain embeddings or use multilingual LLMs

---

## 4️⃣ Scenario: Semantic Search for Support Tickets

### Question:
Your company stores 10k support tickets. You want to allow semantic search using embeddings. Explain how you would use embeddings to retrieve relevant answers.

### Expected Answer:

- Convert tickets into embedding vectors
- Convert user query into embedding vector
- Compute cosine similarity
- Retrieve top-k closest tickets
- Use these as context (if doing RAG)

---

## 5️⃣ Scenario: Prompt Drift in Chatbot Conversations

### Question:
Your chatbot follows initial instructions for 3–4 messages but then begins responding casually or ignoring constraints. Why does this happen and how do you fix it?

### Expected Answer:

- Conversations accumulate → system instruction gets diluted
- **Solutions:**
  - Re-inject system prompt into every message
  - Use "assistant messages" that reinforce behavior
  - Limit conversation history
  - Use explicit rules at each turn

---

## 6️⃣ Scenario: LLM Making Up SQL Queries

### Question:
Your LLM generates incorrect SQL queries when asked to help developers. How to reduce such errors?

### Expected Answer:

- Provide schema in the prompt
- Give good + bad examples
- Use step-by-step reasoning:
  ```
  "First analyze the problem, then write the SQL query."
  ```
- Ask for SQL + explanation
- Add self-review:
  ```
  "Check the SQL for syntax errors before final output."
  ```

---

## 7️⃣ Scenario: LLM API Call Misbehavior

### Question:
Your LLM sometimes returns malformed JSON when calling APIs. What would you do?

### Expected Answer:

- Use function calling (OpenAI) instead of text
- Or use strict JSON prompts
- Validate JSON before use
- Give explicit structure and field descriptions
- Provide failure examples and corrections

---

## 8️⃣ Scenario: Abuse Prevention

### Question:
Your chatbot must avoid answering harmful or controversial questions. How would you enforce safety via prompting?

### Expected Answer:

- System prompt with safety rules
- Explicit forbidden content list
- Few-shot examples showing refusal
- Add classification layer before LLM call
- Add: "If content violates policy, respond with this template: …"

---

# 🧪 HANDS-ON LLM EXERCISES (Beginner → Intermediate)

---

## ⭐ Exercise 1 — Understand Tokenization

### Task:
Take three sentences and tokenize them using the HuggingFace tokenizer.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

sentences = [
    "Machine learning is amazing.",
    "I love transformers!",
    "हिन्दी भाषा सुंदर है।"
]

for s in sentences:
    tokens = tokenizer.tokenize(s)
    print(s, "-->", tokens)
```

### 👉 Observe:

- English vs Hindi differences
- Subword breakdown
- Why multilingual tokenizers are needed

---

## ⭐ Exercise 2 — Compare Embeddings Similarity

Compare similarity between words:

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ["cat", "dog", "car", "engine", "tiger"]

emb = model.encode(sentences, convert_to_tensor=True)
similarities = util.pytorch_cos_sim(emb, emb)

print(similarities)
```

### 👉 Observe that:

- "cat" & "dog" should be closer
- "car" & "engine" also close
- "cat" & "car" far apart

---

## ⭐ Exercise 3 — Build a Prompt with System + User Roles

Use OpenAI API:

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an ML tutor. Be extremely clear and concise."},
        {"role": "user", "content": "Explain attention mechanism in simple terms."}
    ]
)

print(response.choices[0].message["content"])
```

---

## ⭐ Exercise 4 — Few-shot Prompting

Create an LLM that teaches programming concepts using examples.

```
You are an expert Python tutor.

Example:
Q: What is a list comprehension?
A: A shortened syntax to create a new list using a loop.

Q: What is a decorator?
A:
```

### 👉 Ask multiple questions and check consistency.

---

## ⭐ Exercise 5 — Prompt Behavior Test

Create two different system prompts and compare outputs:

### System Prompt A
```
You are a fun, friendly assistant.
```

### System Prompt B
```
You are a strict software architect. Explain only with technical depth.
```

### Task:
Ask:
```
Explain how transformers work.
```

### 👉 Compare:

- Tone
- Depth
- Structure

---

## ⭐ Exercise 6 — Build a Small Q&A Chatbot (NO RAG)

Simple Python code:

```python
from openai import OpenAI
client = OpenAI()

system = """
You are a Q&A assistant.
Rules:
- Do NOT guess.
- If unsure, say: 'I don't have enough information.'
"""

while True:
    q = input("User: ")
    if q.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": q}
        ]
    )
    
    print("Bot:", response.choices[0].message["content"])
```

### Features:

- Uses system instructions
- Simple Q&A
- Guards hallucinations