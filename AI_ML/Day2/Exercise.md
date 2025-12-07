# 🚀 Real-Time Scenario Based Interview Questions (Data Preprocessing + FE)
---

## 1️⃣ Scenario: Dataset Has 30% Missing Values

### Q:
You receive a dataset where 30% of the values in the "Age" column and 15% in "Salary" are missing. What do you do?

### ⭐ Expected Thinking:

- ✔ Identify missing pattern (MCAR/MAR/MNAR)
- ✔ If missingness is high, avoid dropping
- ✔ Use different imputation strategies based on correlation
- ✔ Consider models that handle missing values (e.g., XGBoost)

### 🧪 Hands-On Example: KNN Imputation

```python
from sklearn.impute import KNNImputer
import pandas as pd

imputer = KNNImputer(n_neighbors=5)
df[['Age','Salary']] = imputer.fit_transform(df[['Age','Salary']])
```

---

## 2️⃣ Scenario: Categorical Column has 50+ Unique Values

### Q:
Your "City" column has 50 unique categories. Using One-Hot Encoding will create too many columns. What will you do?

### ⭐ Expected Thinking:

- Use Target Encoding
- Use Feature Hashing
- Group rare categories into "Other"
- Consider frequency encoding

### 🧪 Example: Frequency Encoding

```python
freq = df['City'].value_counts().to_dict()
df['City_freq'] = df['City'].map(freq)
```

---

## 3️⃣ Scenario: Data Leakage Detected

### Q:
You trained a model with high accuracy, but later discovered that you scaled data before splitting. What happened? How do you fix it?

### ⭐ Expected Thinking:

- This caused data leakage
- Test data influenced scaling on train data
- Always scale after splitting using Pipelines

### 🧪 Fix with Pipeline:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression())
])

pipe.fit(X_train, y_train)
```

---

## 4️⃣ Scenario: Outliers Affecting Model Performance

### Q:
Housing price dataset has extreme outliers for "Price". Your model is unstable. What do you do?

### ⭐ Expected Thinking:

- Detect outliers using IQR, Z-score
- Cap using Winsorization
- Treat separately for log-normal distributions
- Use tree-based models (less sensitive)

### 🧪 Hands-On Example: IQR Method

```python
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Price'] >= Q1 - 1.5*IQR) & (df['Price'] <= Q3 + 1.5*IQR)]
```

---

## 5️⃣ Scenario: Scaling Required Only for Numeric Columns

### Q:
You have a mix of numeric and categorical features. How do you scale only numeric columns?

### ⭐ Expected Thinking:

- Use ColumnTransformer
- Apply different transformers per column type

### 🧪 Example:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocess = ColumnTransformer([
    ('num', StandardScaler(), ['Age','Fare']),
    ('cat', OneHotEncoder(), ['Sex','Embarked'])
])
```

---

## 6️⃣ Scenario: Pipeline Needed for Production

### Q:
How do you ensure preprocessing + model training steps remain consistent between training and inference?

### ⭐ Expected Thinking:

- Use sklearn Pipeline
- Use ColumnTransformer
- Preprocessing + model as a single object
- Save complete pipeline using joblib

### 🧪 Example Pipeline:

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('preprocess', preprocess),
    ('model', RandomForestClassifier())
])
```

---

## 7️⃣ Scenario: Too Many Features (Curse of Dimensionality)

### Q:
Dataset contains 2000 features. Model is slow and overfits. What do you do?

### ⭐ Expected Thinking:

- Remove correlated features
- Use PCA
- Use feature importance (tree models, Lasso)

### 🧪 Example: SelectKBest

```python
from sklearn.feature_selection import SelectKBest, chi2

selector = SelectKBest(chi2, k=100)
X_new = selector.fit_transform(X, y)
```

---

## 8️⃣ Scenario: Ordinal Categorical Values

### Q:
Column "Education": ['High School', 'College', 'Masters', 'PhD']  
What encoding should you use?

### ⭐ Expected Thinking:

- Use Ordinal Encoding
- Maintain natural ranking

### 🧪 Example:

```python
from sklearn.preprocessing import OrdinalEncoder

enc = OrdinalEncoder(categories=[['High School', 'College', 'Masters', 'PhD']])
df['Education'] = enc.fit_transform(df[['Education']])
```

---

## 9️⃣ Scenario: Target Leakage in Titanic Dataset

### Q:
You notice that "Cabin" and "Ticket" strongly predict survival but are not realistic features. What will you do?

### ⭐ Expected Thinking:

- Remove columns that don't exist at prediction time
- Avoid features created AFTER the event (leakage)

### 🧪 Example:

```python
df.drop(['Ticket','Cabin'], axis=1, inplace=True)
```

---

## 🔟 Scenario: Feature Engineering Required to Improve Accuracy

### Q:
Titanic dataset: Engineering new features improves model greatly. What features can you create?

### ⭐ Best Features:

- FamilySize = SibSp + Parch + 1
- Title extraction from Name
- Age groups (binning)
- Fare per person
- Deck extraction from Cabin

### 🧪 Example: Family Size

```python
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
```

---

## 1️⃣1️⃣ Scenario: Column "Embarked" has 3 categories + missing values

### Q:
How do you handle this?

### ⭐ Expected Thinking:

- Impute with most frequent
- Apply One-Hot Encoding

### 🧪 Example:

```python
from sklearn.impute import SimpleImputer

imp = SimpleImputer(strategy='most_frequent')
df['Embarked'] = imp.fit_transform(df[['Embarked']])
```

---

## 1️⃣2️⃣ Scenario: Scaling Needed Before KNN Classifier

### Q:
You want to use KNN. Do you need scaling? Why?

### ⭐ Expected Answer:

- YES, KNN is distance-based
- Without scaling, large-range features dominate distance
- Standardization recommended

---

## 💻 Complete Hands-On Example (Real Interview Style)

### 📌 Task: Build a preprocessing pipeline for Titanic dataset + model

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("titanic.csv")

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

X = df[['Pclass','Sex','Age','Fare','Embarked','FamilySize']]
y = df['Survived']

num_cols = ['Age','Fare','FamilySize']
cat_cols = ['Pclass','Sex','Embarked']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ohe', OneHotEncoder())
])

preprocess = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

pipe = Pipeline([
    ('preprocess', preprocess),
    ('model', RandomForestClassifier())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
```