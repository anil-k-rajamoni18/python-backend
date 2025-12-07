# 🌟 DAY 2 — Data Preprocessing + Feature Engineering

---

## 1️⃣ Introduction: Why Data Preprocessing Matters?

> "80% of a data scientist's time is spent on cleaning data, not building models."

Models learn patterns from data — so the quality of the input directly determines model performance.

**Think of it like cooking:**
- 🥕 Fresh ingredients → delicious meal
- 🗑️ Spoiled ingredients → terrible outcome

Same with data → clean data = good model.

---

## 2️⃣ Handling Missing Values

Real-world datasets almost always contain missing values.

### ✅ Why data might be missing?

- Human error (survey forms)
- System/pipeline issues (API not responding)
- Sensor failures
- Corrupted logs

### 📌 Types of Missing Data

| Type | Meaning | Example |
|------|---------|---------|
| MCAR | Missing Completely at Random | Survey question skipped randomly |
| MAR | Missing at Random | Income missing for older people |
| MNAR | Missing Not at Random | People with high income avoid sharing |

### 🛠️ Common Missing Value Techniques

#### 1. Drop missing values

**Use when:**
- Missing % < 5%
- Data missing is random

```python
df.dropna()
```

#### 2. Fill missing values (Imputation)

**Numerical columns:**
- Mean / Median / Mode
- KNN imputer
- Regression imputation

**Categorical columns:**
- Most frequent category
- "Unknown" category

```python
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Gender'].fillna('Unknown', inplace=True)
```

#### 3. Advanced: KNN Imputer

Works well when values depend on neighbors.

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)
df_filled = imputer.fit_transform(df)
```

---

## 3️⃣ Scaling & Normalization

Different features have different ranges:
- **Age:** 0–100
- **Salary:** 0–2,00,000
- **Height:** 120–200 cm

Models get confused due to scale differences (especially KNN, SVM, NN).

### 🧮 Types of Scaling

#### 1. Standardization (Z-score scaling)

```
X' = (X - μ) / σ
```

- **Output:** mean 0, std 1
- **Used in:** SVM, Logistic Regression, Neural Networks

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### 2. Min-Max Scaling

Scales to 0–1

```
X' = (X - X_min) / (X_max - X_min)
```

- **Used in:** Neural networks, distance-based models

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

#### 3. Normalization (L2 norm)

For text vectors, embeddings.

---

## 4️⃣ Encoding Categorical Data

Models cannot understand text → convert to numbers.

### 🧩 Encoding Options

#### 1. Label Encoding

Assigns numeric labels to categories.

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
```

⚠️ **Problem:**  
Models may think "Male=1, Female=0" → numeric priority  
Use only for ordinal categories.

#### 2. One-Hot Encoding

Creates separate columns for each category.

```python
pd.get_dummies(df, columns=['City'])
```

**Good for:** Decision Trees, Random Forest

#### 3. Ordinal Encoding

If categories have rank: Low < Medium < High

```python
from sklearn.preprocessing import OrdinalEncoder

enc = OrdinalEncoder()
df['Education'] = enc.fit_transform(df[['Education']])
```

#### 4. Target Encoding

Replace category with mean of target variable.  
Used in Kaggle competitions.

---

## 5️⃣ Feature Selection & Feature Importance

**Helps:**
- Reduce training time
- Avoid overfitting
- Improve accuracy
- Increase interpretability

### ⭐ Approaches

#### 1. Filter Methods

- Correlation matrix
- Chi-square
- ANOVA

```python
df.corr()
```

#### 2. Wrapper Methods

- Forward Selection
- Backward Elimination
- Recursive Feature Elimination (RFE)

```python
from sklearn.feature_selection import RFE

selector = RFE(model, n_features_to_select=5)
selector.fit(X, y)
```

#### 3. Embedded Methods

- L1 Regularization (Lasso)
- L2 (Ridge)
- Feature importance from Tree models

```python
model.feature_importances_
```

---

## 6️⃣ Train Pipeline Automation

Manual preprocessing leads to errors.  
Instead: automate using scikit-learn Pipelines

### 🚀 Pipeline Benefits

- Ensures same transformations applied on train & test
- No leakage
- Clean, production-ready
- Easy hyperparameter tuning with GridSearchCV

### 🛠️ Example Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
pipe.predict(X_test)
```

### 🚀 Full Feature Engineering + Pipeline Example

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

numeric_features = ['Age', 'Fare']
categorical_features = ['Sex', 'Embarked']

numeric_transformer = Pipeline([
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

pipe = Pipeline([
    ('preprocess', preprocessor),
    ('model', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
```

---

## 7️⃣ Hands-On Tasks

### 🔧 Task 1: Clean a Messy Dataset

**Steps:**
1. Remove duplicates
2. Handle missing values with different strategies
3. Remove outliers using IQR
4. Encode categorical variables
5. Scale numerical columns
6. Split into train/test

### 🔧 Task 2: Build Feature Engineering Pipeline

1. Create pipelines for numeric & categorical features
2. Combine with ColumnTransformer
3. Add classifier (RandomForest or Logistic Regression)
4. Train and evaluate

---

## 🎯 Mini Project — Titanic Survival Prediction

### 📌 Objective

Predict if a passenger survived based on:
- Age
- Sex
- Fare
- Passenger class
- Family size
- Embarkation port

### 📊 Steps

#### 1. Load dataset

```python
import pandas as pd

df = pd.read_csv('titanic.csv')
```

#### 2. Feature Engineering

- Extract Title from Name
- FamilySize = SibSp + Parch + 1
- Age missing value imputation
- Encode Sex, Embarked

#### 3. Pipeline Preprocessing

```python
num_cols = ['Age', 'Fare', 'FamilySize']
cat_cols = ['Sex', 'Pclass', 'Embarked']

num_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ohe', OneHotEncoder())
])

preprocessor = ColumnTransformer([
    ('num', num_transformer, num_cols),
    ('cat', cat_transformer, cat_cols)
])
```

#### 4. Combine with Model

```python
pipe = Pipeline([
    ('preprocess', preprocessor),
    ('clf', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
```

#### 5. Evaluate Accuracy

```python
from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, pred))
```

---

## 🎉 End of Day 2 Summary

By now, students understand:

- ✔ Handling missing values
- ✔ Scaling, normalization, encoding
- ✔ Outlier detection
- ✔ Feature selection methods
- ✔ How to build ML pipelines
- ✔ Real-world preprocessing workflows
- ✔ Completed Titanic Prediction mini-project