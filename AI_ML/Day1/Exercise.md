# 🚀 Scenario-Based ML Interview Questions + Hands-On Examples

---

## 1️⃣ Scenario: Model Performance Drops in Production

### 🔸 Question:
Your ML model shows 95% accuracy during training & testing but drops to 70% after deployment. What could be the reasons? How will you fix it?

### ✔ Expected Answer (Key Points)

**Possible causes:**
- Data drift (live data distribution ≠ training data)
- Concept drift (relationship between input → output changed)
- Model overfitting
- Poor generalization due to biased sample
- Changes in upstream data pipeline (feature missing)
- API or serialization issues

**Fix using:**
- Retrain on recent data
- Monitor drift using KL divergence/PSI
- Add robust validation
- Cross-check feature schema using tools like TF Data Validation

---

## 2️⃣ Scenario: Class Imbalance Problem

### 🔸 Question:
You are building a fraud detection model. Only 1% transactions are fraud. Accuracy gives misleading results. What do you do?

### ✔ Expected Answer

- Use Precision, Recall, F1, ROC-AUC
- Apply oversampling (SMOTE) or undersampling
- Try cost-sensitive learning
- Try anomaly detection models
- Evaluate using confusion matrix

### 🧪 Hands-On Example (SMOTE)

```python
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

sm = SMOTE()

X_res, y_res = sm.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
```

---

## 3️⃣ Scenario: Overfitting Detected During Training

### 🔸 Question:
Train accuracy = 98%  
Test accuracy = 70%  
How do you solve overfitting?

### ✔ Expected Answer

- Use regularization (L1/L2)
- Early stopping
- Simplify model
- Increase training data
- Use dropout (for neural networks)
- Cross-validation

### 🧪 Hands-On Example (Regularization)

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C=0.1)  # stronger regularization
model.fit(X_train, y_train)
```

---

## 4️⃣ Scenario: Your Model Takes Too Long To Train

### 🔸 Question:
You're training a Random Forest on 5 million rows. It takes too long. How do you speed it up?

### ✔ Expected Answer

- Reduce dataset using sampling
- Use PCA/dimensionality reduction
- Use distributed training (Spark ML)
- Reduce number of trees
- Use parallel processing (n_jobs=-1 in sklearn)
- Move to faster models (XGBoost, LightGBM)

### 🧪 Hands-On Example (Speed up Random Forest)

```python
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    n_jobs=-1
)
```

---

## 5️⃣ Scenario: Choosing the Right Algorithm

### 🔸 Question:
Your dataset has:
- 1000 samples
- 200 features
- Binary classification
- You want interpretability + speed

Which model will you choose?

### ✔ Expected Answer

- Logistic Regression (high interpretability)
- Linear SVM
- Decision Tree for rule-based interpretability
- Avoid deep learning (low data)

---

## 6️⃣ Scenario: Predicting House Prices (Regression Problem)

### 🔸 Question
How do you evaluate your regression model? Which metrics?

### ✔ Expected Answer

- MAE
- MSE
- RMSE
- R² Score

### 🧪 Hands-On Example (Regression Evaluation)

```python
from sklearn.metrics import mean_absolute_error, r2_score

pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred))
print("R2:", r2_score(y_test, pred))
```

---

## 7️⃣ Scenario: Missing Values in Dataset

### 🔸 Question
Your dataset has 30% missing values in 3 important columns. What will you do?

### ✔ Expected Answer

- Drop only if missingness is random & <10%
- Impute using:
  - Mean/median
  - KNN imputer
  - Regression imputation
- Use algorithms that handle missing values (XGBoost)

### 🧪 Example (Using KNN Imputer)

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)
```

---

## 8️⃣ Scenario: Feature Importance Needed

### 🔸 Question
The client wants to know which features affect the loan approval most. How do you find feature importance?

### ✔ Expected Answer

- Use RandomForest feature importance
- Use SHAP values
- Use permutation importance

### 🧪 Hands-On Example (SHAP)

```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

---

## 9️⃣ Scenario: Deploying ML Model

### 🔸 Question
How do you deploy a model to production?

### ✔ Expected Answer

- Save model using joblib/pickle
- Create REST API using Flask/FastAPI
- Containerize with Docker
- Monitor model performance via logs

---

## 🔟 Scenario: Dataset Has High Dimensionality (1000+ Features)

### 🔸 Question
How do you reduce dimensionality and why?

### ✔ Expected Answer

- PCA
- Autoencoders
- Feature selection (L1 penalty)
- Remove multicollinearity

### 🧪 PCA Example

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=50)
X_reduced = pca.fit_transform(X)
```

---

## 1️⃣1️⃣ Scenario: Choosing Metrics Based on Use-Case

### 🔸 Question
You are working on:
- Medical diagnosis model
- Spam classification
- Credit fraud detection

Which metric will you prioritize?

### ✔ Expected Answer

| Use Case | Metric |
|----------|--------|
| Medical diagnosis | Recall (avoid false negatives!) |
| Spam detection | Precision (avoid marking legit mail as spam) |
| Fraud detection | F1 Score / Recall |

---

## 1️⃣2️⃣ Scenario: Drift Detection in Production

### 🔸 Question
If your model suddenly becomes inaccurate after 6 months, how do you check if data drift occurred?

### ✔ Expected Answer

- Compare train vs live data distribution
- Use:
  - Population Stability Index (PSI)
  - KL Divergence
  - Kolmogorov–Smirnov Test
- Create dashboards for automated drift alerts

---

## 1️⃣3️⃣ Scenario: Manual Mistake in Data Pipeline

### 🔸 Question
You notice your model prediction is always wrong for last few days. How do you debug?

### ✔ Expected Answer

- Check feature schema mismatch
- Check if columns order changed
- Check if scaling was applied incorrectly
- Inspect raw data → feature extraction pipeline

---

## 1️⃣4️⃣ Scenario-Based Coding Question

### 🔸 Question
Build a model to classify customers as churn or not. Evaluate using F1 score because dataset is imbalanced.

### 🧪 Hands-On Code

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import GradientBoostingClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GradientBoostingClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("F1 Score:", f1_score(y_test, pred))
```

---

## 🎁 Bonus: Behavioral + Scenario ML Questions

⭐ **"Tell me about a time your model failed. What did you do?"**

⭐ **"Describe the most challenging dataset you handled."**

⭐ **"How do you explain a model's decision to a non-technical client?"**

⭐ **"How do you handle disagreements with Product/Business teams?"**

⭐ **"Describe a case where you improved accuracy significantly."**

> Each of these tests not just your technical skill, but communication & problem-solving.