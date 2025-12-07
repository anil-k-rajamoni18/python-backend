# 🌟 DAY 1 — AI & ML FOUNDATIONS (Core Basics)

---

## 1️⃣ What is AI, ML, and Deep Learning?

### 🤖 Artificial Intelligence (AI)

AI is the broad field where machines are designed to mimic human intelligence.

**Real-world examples:**
- Siri/Alexa answering questions
- Google Maps predicting traffic
- Netflix recommending shows

> AI = Big umbrella → ML is one branch inside it.

### 📘 Machine Learning (ML)

ML is a subset of AI where machines learn patterns from data rather than being explicitly programmed.

**Simple analogy:**  
Think of ML as teaching a child by showing examples rather than giving rules.

**Real example:**  
Email spam detection → The model sees thousands of "spam" and "not spam" emails and learns patterns.

### 🧠 Deep Learning (DL)

DL is a subset of ML based on Neural Networks with many layers.

**When to use DL:**
- Large datasets
- Complex patterns
- Images, audio, text

**Examples:**
- Face recognition
- Self-driving cars detecting objects
- ChatGPT (Large neural networks)

---

## 2️⃣ Types of Machine Learning

### 1. Supervised Learning

Model learns from labeled data → Each input has an output.

**Examples:**
- Predict house prices
- Classify emails (spam / not spam)
- Detect fraud in transactions

**Algorithms:** Linear Regression, Decision Trees, SVM, Random Forest, Neural Networks.

### 2. Unsupervised Learning

Model learns patterns from unlabeled data (no output provided).

**Examples:**
- Customer segmentation in marketing
- Anomaly detection in credit card usage
- Grouping similar products on e-commerce

**Algorithms:** K-Means, PCA, Hierarchical Clustering.

### 3. Reinforcement Learning

Model learns by interacting with an environment and receiving rewards/punishments.

**Examples:**
- Game AI (Chess, Go)
- Robot learning to walk
- Google DeepMind controlling cooling systems

**Analogy:**  
A dog learns tricks through rewards → RL works the same way.

---

## 3️⃣ ML Pipeline Overview

The typical ML workflow:

1. Define Problem
2. Collect Data
3. Clean & Preprocess Data
4. Split Data (Train/Val/Test)
5. Select Algorithm
6. Train Model
7. Evaluate
8. Tune Hyperparameters
9. Deploy
10. Monitor & Maintain

**Real Example (Bank Loan Approval):**
- Collect customer data
- Clean missing values
- Train/validate a classifier
- Deploy model to loan portal

---

## 4️⃣ What is a Model? What are Parameters & Weights?

### 🎯 Model

A model is a mathematical function that maps inputs → output.

**Example:**
- **Input (features):** Age, Salary, Credit Score
- **Output:** Approve or Reject

### ⚙️ Parameters / Weights

Values learned by the model during training.

**Example:**  
In Linear Regression:

```
y = w₁x₁ + w₂x₂ + b
```

- `w₁, w₂` are weights
- `b` is bias
- These adjust during training to reduce error.

### 🎛️ Hyperparameters

Settings chosen by the developer → not learned by model.

**Examples:**
- Learning rate
- Number of tree depth
- Number of clusters (K in K-Means)

---

## 5️⃣ Train / Validation / Test Split

To avoid overfitting and evaluate fairly:

| Split Type | Purpose | Typical Size |
|------------|---------|--------------|
| Training | Learn model parameters | 70% |
| Validation | Tune hyperparameters | 15% |
| Test | Final unbiased evaluation | 15% |

**Real Example:**  
Like studying for an exam:
- **Train** = practice questions
- **Validation** = mock test
- **Test** = final exam

---

## 6️⃣ Model Evaluation Metrics

### ✔️ Accuracy

```
Accuracy = Correct Predictions / Total Predictions
```

Good when classes are balanced.

### 🎯 Precision

Out of predicted positives, how many were actually positive?

- Used when false positives are costly.
- **Example:** Fraud detection.

### 🔍 Recall

Out of actual positives, how many did the model correctly find?

- Used when false negatives are costly.
- **Example:** Cancer detection.

### 🧮 F1 Score

Harmonic mean of precision and recall.  
Useful when classes are imbalanced.

---

## 7️⃣ Tools Covered Today

- 🔹 **Python** — Standard ML programming language.
- 🔹 **scikit-learn** — Most popular ML library for classical algorithms.
- 🔹 **Jupyter Notebook / Google Colab** — Interactive coding environments ideal for ML training.

---

## 8️⃣ Hands-On Tasks (Practice)

Below is the exact flow for the session.

### 🔹 1. Load dataset from sklearn

```python
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target
```

### 🔹 2. Train/Test Split

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 🔹 3. Train a classifier

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

### 🔹 4. Evaluate accuracy

```python
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

---

## 9️⃣ Mini Project – Iris Classifier (sklearn)

📌 **Goal:** Build a model to classify Iris flower species based on 4 features.

**Features:**
- Sepal length
- Sepal width
- Petal length
- Petal width

**Output:**
- Iris Setosa
- Iris Versicolor
- Iris Virginica

### ✔️ Full Code

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

### 🎉 Output Insight

- Accuracy often ~95–100%
- Shows model is highly effective on Iris dataset

---

## 🎯 End of Day 1 Summary

By the end of Day 1, learners understand:

- ✔ AI, ML, DL fundamentals
- ✔ ML types and pipeline
- ✔ What models/weights/hyperparameters mean
- ✔ How to train, test, and evaluate an ML model
- ✔ Hands-on using sklearn
- ✔ Completed a real mini-project (Iris Classifier)