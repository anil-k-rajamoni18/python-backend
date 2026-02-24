# 🚀 30-Day AI / ML / Generative AI Learning Roadmap
### From Scratch → Production-Ready Skills

> **Who is this for?** Complete beginners with basic Python knowledge who want to master AI, ML, and Generative AI from the ground up.
> 
> **Structure:** Each day = Theory + Example + Hands-On + Exercise | Every Week = Mini Project

---

## 📅 WEEK 1 — Foundations of AI & Machine Learning
> **Theme:** Understand what AI/ML is, the math behind it, and build your first models.

---

### Day 1 — What is AI, ML, and Deep Learning?

#### 🧠 Theory
- Difference between AI, ML, DL, and Gen-AI
- Types of Machine Learning: Supervised, Unsupervised, Reinforcement
- Real-world applications: self-driving cars, recommendation systems, chatbots
- The ML Pipeline: Data → Model → Train → Evaluate → Deploy

#### 💡 Example
```
AI = Broad field (machines simulating human intelligence)
ML = Subset of AI (machines learn from data)
DL = Subset of ML (uses neural networks with many layers)
Gen-AI = Subset of DL (generates new content: text, images, code)
```

#### 🛠️ Hands-On
```python
# Set up your environment
pip install numpy pandas matplotlib scikit-learn jupyter

# Launch Jupyter
jupyter notebook

# Hello World of ML
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
```

#### 📝 Exercise
- Write a 1-page summary: "3 AI applications that excite you and why"
- Identify which type of ML (supervised/unsupervised/RL) each application uses

---

### Day 2 — Python & NumPy for ML

#### 🧠 Theory
- Why Python is the language of AI/ML
- NumPy arrays vs Python lists (speed, vectorization)
- Broadcasting, slicing, reshaping
- Random number generation for ML

#### 💡 Example
```python
import numpy as np

# Vectorized operations (much faster than loops)
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
dot_product = np.dot(a, b)  # 550
```

#### 🛠️ Hands-On
```python
import numpy as np

# Create and manipulate arrays
matrix = np.random.randn(5, 3)       # 5x3 matrix with normal distribution
print("Shape:", matrix.shape)
print("Mean:", matrix.mean(axis=0))   # column-wise mean
print("Std:", matrix.std())

# Matrix multiplication (core of neural networks)
W = np.random.randn(3, 2)            # weights
output = matrix @ W                  # 5x2 result
print("Output shape:", output.shape)

# Useful functions
normalized = (matrix - matrix.mean()) / matrix.std()  # Z-score normalization
```

#### 📝 Exercise
- Create a 10x10 matrix, compute row-wise sum, column-wise max, and the overall median
- Implement vector cosine similarity from scratch using NumPy

---

### Day 3 — Data Exploration with Pandas & Matplotlib

#### 🧠 Theory
- DataFrames and Series
- Exploratory Data Analysis (EDA): distributions, correlations, missing values
- Data cleaning: handling nulls, duplicates, outliers
- Visualization: why it matters before modeling

#### 💡 Example
```python
# EDA workflow
df.info()          # data types and nulls
df.describe()      # statistical summary
df.isnull().sum()  # count missing values per column
df.corr()          # correlation matrix
```

#### 🛠️ Hands-On
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a real dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# EDA
print(df.shape)
print(df.isnull().sum())
print(df['Survived'].value_counts())

# Visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

df['Age'].hist(bins=30, ax=axes[0], title='Age Distribution')
df['Survived'].value_counts().plot(kind='bar', ax=axes[1], title='Survival Count')
sns.heatmap(df[['Age', 'Fare', 'Pclass', 'Survived']].corr(), 
            annot=True, ax=axes[2])
plt.tight_layout()
plt.show()
```

#### 📝 Exercise
- Download the Titanic dataset
- Answer: What's the survival rate by gender? By class? Plot both.
- Clean the dataset: fill missing Ages with median, drop Cabin column

---

### Day 4 — Linear Regression

#### 🧠 Theory
- What is regression? Predicting continuous values
- The equation: y = mx + b (and multi-dimensional version)
- Cost function: Mean Squared Error (MSE)
- Gradient Descent: how models learn
- Overfitting vs Underfitting, Train/Test split

#### 💡 Example
```
House Price Prediction:
Price = (w1 × size) + (w2 × bedrooms) + (w3 × location_score) + bias

Goal: Find the best w1, w2, w3 that minimizes prediction error
```

#### 🛠️ Hands-On
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Train model
model = LinearRegression()
model.fit(X, y)

print(f"Intercept: {model.intercept_[0]:.2f}")  # should be ~4
print(f"Coefficient: {model.coef_[0][0]:.2f}")  # should be ~3

# Evaluate
y_pred = model.predict(X)
print(f"MSE: {mean_squared_error(y, y_pred):.4f}")
print(f"R² Score: {r2_score(y, y_pred):.4f}")

# From scratch
def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, b = 0, 0
    n = len(X)
    for _ in range(epochs):
        y_pred = m * X + b
        dm = (-2/n) * sum(X * (y - y_pred))
        db = (-2/n) * sum(y - y_pred)
        m -= lr * dm
        b -= lr * db
    return m, b
```

#### 📝 Exercise
- Predict housing prices using the Boston Housing dataset
- Plot the regression line against actual data points
- Experiment: what happens to R² when you add noise to the data?

---

### Day 5 — Classification with Logistic Regression & Decision Trees

#### 🧠 Theory
- Classification vs Regression
- Sigmoid function and probability outputs
- Decision Trees: splitting on features, information gain, Gini impurity
- Evaluation metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

#### 💡 Example
```
Spam Detection:
Input: email features (keyword counts, sender reputation)
Output: 0 (not spam) or 1 (spam)

Sigmoid: σ(z) = 1 / (1 + e^(-z))  → always between 0 and 1
```

#### 🛠️ Hands-On
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
lr = LogisticRegression(max_iter=10000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Decision Tree
dt = DecisionTreeClassifier(max_depth=4)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("Logistic Regression Report:")
print(classification_report(y_test, y_pred_lr))

print("Decision Tree Report:")
print(classification_report(y_test, y_pred_dt))

# Visualize Decision Tree
plt.figure(figsize=(20, 10))
plot_tree(dt, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()
```

#### 📝 Exercise
- Build a classifier to predict Titanic survival
- Calculate Precision, Recall, F1 manually from the confusion matrix
- What does it mean if Recall is high but Precision is low?

---

### Day 6 — Feature Engineering & Data Preprocessing

#### 🧠 Theory
- Feature scaling: Min-Max Normalization, Standardization (Z-score)
- Encoding categorical variables: One-Hot, Label Encoding, Ordinal
- Feature selection: correlation, feature importance
- Handling imbalanced datasets: SMOTE, class weights
- Pipelines in scikit-learn

#### 💡 Example
```
Raw data: City = ["Mumbai", "Delhi", "Bangalore"]
One-Hot: Mumbai=[1,0,0], Delhi=[0,1,0], Bangalore=[0,0,1]

Why scale? If "salary" is in thousands and "age" is in years,
gradient descent will struggle — scaling makes them comparable.
```

#### 🛠️ Hands-On
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd

# Sample data
data = {
    'age': [25, 45, 35, 22, 58],
    'salary': [50000, 120000, 80000, 35000, 150000],
    'city': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi'],
    'target': [0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Define transformers
numeric_features = ['age', 'salary']
categorical_features = ['city']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

# Build pipeline
from sklearn.tree import DecisionTreeClassifier
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier())
])

X = df[['age', 'salary', 'city']]
y = df['target']
pipeline.fit(X, y)
print("Predictions:", pipeline.predict(X))
```

#### 📝 Exercise
- Take the Titanic dataset, create a full preprocessing pipeline
- Engineer a new feature: FamilySize = SibSp + Parch + 1
- Compare model accuracy before and after feature engineering

---

### Day 7 — 🏆 WEEK 1 MINI PROJECT: End-to-End ML Pipeline

#### Project: Customer Churn Prediction

**Goal:** Predict which telecom customers will churn (cancel service)

**Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

```python
# WEEK 1 MINI PROJECT — Customer Churn Prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, roc_auc_score, roc_curve

# === STEP 1: Load & Explore ===
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.shape, df.dtypes, df.isnull().sum())

# === STEP 2: Clean ===
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop('customerID', axis=1, inplace=True)

# === STEP 3: Encode ===
le = LabelEncoder()
binary_cols = [c for c in df.select_dtypes('object').columns if df[c].nunique() == 2]
for col in binary_cols:
    df[col] = le.fit_transform(df[col])

df = pd.get_dummies(df, drop_first=True)

# === STEP 4: Train/Test Split ===
X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === STEP 5: Scale ===
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# === STEP 6: Train & Evaluate ===
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(max_depth=5)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n{name}")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1]):.4f}")
```

**Deliverables:**
- [ ] EDA with 5 visualizations
- [ ] Cleaned and preprocessed dataset
- [ ] 2 trained models with comparison
- [ ] Business insight: "Which features most predict churn?"

---

## 📅 WEEK 2 — Advanced ML & Neural Network Foundations
> **Theme:** Ensemble methods, SVMs, intro to neural networks and deep learning.

---

### Day 8 — Ensemble Methods: Random Forest & Gradient Boosting

#### 🧠 Theory
- Ensemble learning: combining weak learners into a strong learner
- Bagging (Random Forest): parallel, reduces variance
- Boosting (XGBoost, AdaBoost): sequential, reduces bias
- Feature importance visualization
- Hyperparameter tuning: GridSearchCV, RandomizedSearchCV

#### 💡 Example
```
Random Forest = Majority vote from 100 decision trees
XGBoost = Each new tree corrects the errors of previous trees

Think of it as:
RF: 100 independent doctors each give diagnosis → majority wins
XGBoost: Doctor 1 diagnoses, Doctor 2 focuses on Doctor 1's mistakes, etc.
```

#### 🛠️ Hands-On
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
import pandas as pd

# Load data
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = data.data, data.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
print(f"RF Accuracy: {rf.score(X_test, y_test):.4f}")

# Feature Importance
import matplotlib.pyplot as plt
feat_imp = pd.Series(rf.feature_importances_, index=data.feature_names).sort_values(ascending=False)
feat_imp[:10].plot(kind='bar', title='Top 10 Features')
plt.tight_layout()
plt.show()

# XGBoost
model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)
model.fit(X_train, y_train)
print(f"XGBoost Accuracy: {model.score(X_test, y_test):.4f}")

# Grid Search
params = {'max_depth': [3, 5, 7], 'n_estimators': [50, 100, 200]}
grid = GridSearchCV(RandomForestClassifier(), params, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)
print("Best params:", grid.best_params_)
```

#### 📝 Exercise
- Compare RF vs XGBoost on the Titanic dataset
- Tune XGBoost with RandomizedSearchCV (50 iterations)
- Plot feature importances for both models

---

### Day 9 — Support Vector Machines & K-Means Clustering

#### 🧠 Theory
- SVM: finding the optimal hyperplane with maximum margin
- Kernel trick: mapping data to higher dimensions (RBF, Polynomial)
- K-Means: unsupervised clustering algorithm
- Elbow method to find optimal K
- Silhouette score for cluster quality

#### 💡 Example
```
SVM analogy: Draw the widest possible street between two neighborhoods
The support vectors are the houses closest to the street boundary

K-Means: Group 1000 customers into 5 segments based on behavior
→ Marketing can then target each segment differently
```

#### 🛠️ Hands-On
```python
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

# SVM Classification
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=200, noise=0.15, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

svm = SVC(kernel='rbf', C=1.0, gamma='scale')
svm.fit(X_scaled, y)
print(f"SVM Accuracy: {svm.score(X_scaled, y):.4f}")

# K-Means Clustering with Elbow Method
from sklearn.datasets import make_blobs
X_cluster, _ = make_blobs(n_samples=300, centers=4, random_state=42)

inertia = []
sil_scores = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster)
    inertia.append(km.inertia_)
    sil_scores.append(silhouette_score(X_cluster, km.labels_))

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('K'); plt.ylabel('Inertia'); plt.title('Elbow Method')

plt.subplot(1, 2, 2)
plt.plot(K_range, sil_scores, 'ro-')
plt.xlabel('K'); plt.ylabel('Silhouette Score'); plt.title('Silhouette Score')
plt.tight_layout()
plt.show()
```

#### 📝 Exercise
- Use K-Means to segment customers from the Mall Customers dataset
- Visualize clusters with a 2D scatter plot
- Write a business interpretation for each cluster

---

### Day 10 — Introduction to Neural Networks

#### 🧠 Theory
- Biological neurons vs artificial neurons
- Perceptron: the simplest neural network
- Layers: Input → Hidden → Output
- Activation functions: ReLU, Sigmoid, Tanh, Softmax
- Forward propagation: how data flows through the network
- Backpropagation & the chain rule: how networks learn

#### 💡 Example
```
Neural Net for digit recognition:
- Input layer: 784 neurons (28x28 pixel image)
- Hidden layer 1: 128 neurons (ReLU activation)
- Hidden layer 2: 64 neurons (ReLU activation)  
- Output layer: 10 neurons (Softmax → probability for each digit 0-9)
```

#### 🛠️ Hands-On
```python
# Build a neural network from scratch (no frameworks)
import numpy as np

def sigmoid(z): return 1 / (1 + np.exp(-z))
def relu(z): return np.maximum(0, z)
def softmax(z): exp_z = np.exp(z - np.max(z)); return exp_z / exp_z.sum()

class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
    
    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2
    
    def loss(self, y_true, y_pred):
        return -np.mean(y_true * np.log(y_pred + 1e-8) + (1-y_true) * np.log(1-y_pred + 1e-8))

# Test it
nn = SimpleNN(input_size=3, hidden_size=4, output_size=1)
X = np.random.randn(10, 3)
y = np.random.randint(0, 2, (10, 1))
output = nn.forward(X)
print(f"Loss: {nn.loss(y, output):.4f}")
```

#### 📝 Exercise
- Draw a neural network architecture for: "Is this email spam?"
- Implement forward propagation for a 2-layer net with sigmoid activation
- Experiment: does increasing hidden size always improve results?

---

### Day 11 — Deep Learning with TensorFlow/Keras

#### 🧠 Theory
- TensorFlow vs PyTorch: ecosystem overview
- Keras API: Sequential and Functional
- Layers: Dense, Dropout, BatchNormalization
- Optimizers: Adam, SGD, RMSprop
- Loss functions: CrossEntropy, MSE, MAE
- Callbacks: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

#### 💡 Example
```python
model = Sequential([
    Dense(128, activation='relu'),  # learns features
    Dropout(0.3),                   # prevents overfitting
    Dense(64, activation='relu'),
    Dense(10, activation='softmax') # 10 class classification
])
```

#### 🛠️ Hands-On
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# Load MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess
X_train = X_train.reshape(-1, 784) / 255.0
X_test = X_test.reshape(-1, 784) / 255.0

# Build model
model = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train with early stopping
es = EarlyStopping(patience=5, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=50, batch_size=128, 
                    validation_split=0.1, callbacks=[es], verbose=1)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

# Plot learning curves
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Val')
plt.title('Accuracy'); plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Val')
plt.title('Loss'); plt.legend()
plt.show()
```

#### 📝 Exercise
- Modify the MNIST model: add more layers, change dropout rate
- Try different optimizers (Adam vs SGD) and compare convergence speed
- What happens when you remove BatchNormalization?

---

### Day 12 — Convolutional Neural Networks (CNNs)

#### 🧠 Theory
- Why CNNs for images? Spatial hierarchy
- Convolution operation: filters, feature maps, stride, padding
- Pooling: MaxPooling, AveragePooling
- CNN architecture: Conv → Pool → Conv → Pool → Flatten → Dense
- Transfer Learning: using pre-trained models (VGG, ResNet, MobileNet)

#### 💡 Example
```
First Conv Layer: detects edges, colors
Second Conv Layer: detects shapes (circles, lines)
Third Conv Layer: detects parts (eyes, wheels)
Output Layer: classifies object (cat, car, bird)

Transfer Learning: A model trained on 1M images already knows
edges, shapes, parts. Just retrain the final layer for YOUR task.
```

#### 🛠️ Hands-On
```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

# CNN from scratch on CIFAR-10
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.4),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=15, batch_size=64, validation_split=0.1)

# Transfer Learning with MobileNetV2
base_model = MobileNetV2(input_shape=(32, 32, 3), include_top=False, weights='imagenet')
base_model.trainable = False  # freeze pretrained weights

tl_model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

tl_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(tl_model.summary())
```

#### 📝 Exercise
- Visualize the filters learned in the first Conv layer
- Implement data augmentation (rotation, flipping, zoom)
- Compare: CNN from scratch vs MobileNetV2 transfer learning (accuracy and training time)

---

### Day 13 — Recurrent Neural Networks & LSTMs

#### 🧠 Theory
- Sequential data: text, time series, speech
- Vanishing gradient problem in plain RNNs
- LSTM: forget gate, input gate, output gate, cell state
- GRU: simplified LSTM
- Applications: sentiment analysis, stock prediction, machine translation

#### 💡 Example
```
Predicting the next word:
"The cat sat on the ___"

LSTM processes: "The" → "cat" → "sat" → "on" → "the"
At each step it updates its memory (cell state)
After "the mat" vs "the floor" patterns — it predicts "mat" or "floor"
```

#### 🛠️ Hands-On
```python
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# LSTM for Time Series: Sine Wave Prediction
# Generate data
timesteps = 1000
t = np.linspace(0, 100, timesteps)
signal = np.sin(t) + 0.1 * np.random.randn(timesteps)

# Create sequences
def create_sequences(data, seq_len=20):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len])
    return np.array(X), np.array(y)

X, y = create_sequences(signal, seq_len=20)
X = X.reshape(-1, 20, 1)

split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM model
model = models.Sequential([
    layers.LSTM(64, input_shape=(20, 1), return_sequences=True),
    layers.LSTM(32),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

y_pred = model.predict(X_test)
plt.figure(figsize=(12, 4))
plt.plot(y_test[:100], label='True')
plt.plot(y_pred[:100], label='Predicted')
plt.legend(); plt.title('LSTM Time Series Prediction')
plt.show()
```

#### 📝 Exercise
- Use LSTM for sentiment analysis on the IMDB dataset (built into Keras)
- Plot the confusion matrix for positive vs negative reviews
- Try GRU instead of LSTM — which performs better?

---

### Day 14 — 🏆 WEEK 2 MINI PROJECT: Image Classifier App

#### Project: Dog vs Cat Classifier with Transfer Learning

**Goal:** Build a web-ready image classifier using MobileNetV2

```python
# WEEK 2 MINI PROJECT — Dog vs Cat Classifier
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    validation_split=0.2
)

# Use Kaggle Dogs vs Cats dataset or any binary image folder
# train_generator = train_datagen.flow_from_directory(...)

# Build model
base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.BatchNormalization(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')  # binary output
])

model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),
              loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.AUC()])

# Fine-tuning phase: unfreeze top layers
base_model.trainable = True
for layer in base_model.layers[:-30]:
    layer.trainable = False

model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
              loss='binary_crossentropy', metrics=['accuracy'])

print(model.summary())
print("Model ready for training on your image dataset!")
```

**Deliverables:**
- [ ] Data augmentation pipeline
- [ ] Transfer learning model
- [ ] Fine-tuned model (unfreeze last 30 layers)
- [ ] Predict on 5 custom images
- [ ] Compare: scratch CNN vs MobileNetV2 (accuracy, training time)

---

## 📅 WEEK 3 — Natural Language Processing & Transformers
> **Theme:** Text processing, NLP fundamentals, attention mechanisms, and Transformer models.

---

### Day 15 — NLP Fundamentals

#### 🧠 Theory
- Text preprocessing: tokenization, stopwords, stemming, lemmatization
- Bag of Words (BoW) and TF-IDF
- Word embeddings: Word2Vec, GloVe — why they're better than BoW
- Text classification pipeline
- Named Entity Recognition (NER), POS tagging

#### 💡 Example
```
Raw text: "The cats are running quickly"
Tokenize: ["The", "cats", "are", "running", "quickly"]
Remove stopwords: ["cats", "running", "quickly"]
Lemmatize: ["cat", "run", "quickly"]

TF-IDF insight: "machine" in an ML paper = high IDF score
               "the" everywhere = very low IDF score
```

#### 🛠️ Hands-On
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nltk.download(['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger'])

# Preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# Sample data
docs = [
    "I love machine learning and AI",
    "Python is great for data science",
    "Football and basketball are popular sports",
    "The team scored a goal in the final match"
]

processed = [preprocess(d) for d in docs]
print(processed)

# TF-IDF + Classifier Pipeline
texts = ["great movie loved it", "terrible film waste of time", 
         "amazing story great acting", "boring and slow bad film"]
labels = [1, 0, 1, 0]  # 1=positive, 0=negative

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
    ('clf', MultinomialNB())
])
pipeline.fit(texts, labels)
print(pipeline.predict(["excellent brilliant loved it"]))
```

#### 📝 Exercise
- Preprocess and classify the 20 Newsgroups dataset (built into sklearn)
- Compare BoW vs TF-IDF for accuracy
- Implement a simple keyword-based sentiment analyzer

---

### Day 16 — Word Embeddings & Word2Vec

#### 🧠 Theory
- Why one-hot vectors fail: no semantic meaning, high dimensionality
- Word2Vec: CBOW vs Skip-gram architectures
- The famous analogy: King - Man + Woman = Queen
- Cosine similarity for word relationships
- Pre-trained embeddings: GloVe, FastText

#### 💡 Example
```python
# Word2Vec captures meaning:
model['king'] - model['man'] + model['woman'] ≈ model['queen']
model['paris'] - model['france'] + model['germany'] ≈ model['berlin']

# Similar words:
model.most_similar('python') → [('java', 0.85), ('programming', 0.82)]
```

#### 🛠️ Hands-On
```python
from gensim.models import Word2Vec
import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

# Train Word2Vec on custom corpus
sentences = [
    ["machine", "learning", "is", "fascinating"],
    ["deep", "learning", "uses", "neural", "networks"],
    ["natural", "language", "processing", "handles", "text"],
    ["python", "is", "used", "for", "machine", "learning"],
    ["data", "science", "combines", "statistics", "and", "programming"]
]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, epochs=100)
print("Similarity (machine, learning):", model.wv.similarity('machine', 'learning'))
print("Most similar to 'learning':", model.wv.most_similar('learning', topn=3))

# Load pretrained GloVe
glove = api.load('glove-wiki-gigaword-50')
print("\nGloVe analogy - king-man+woman:", 
      glove.most_similar(positive=['king', 'woman'], negative=['man'], topn=1))

# Visualize with PCA
words = ['machine', 'learning', 'deep', 'neural', 'data', 'python', 'network']
vectors = [glove[w] for w in words]
pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)

plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.annotate(word, (reduced[i, 0], reduced[i, 1]), fontsize=12)
plt.scatter(reduced[:, 0], reduced[:, 1])
plt.title('Word Embeddings Visualized (PCA)')
plt.show()
```

#### 📝 Exercise
- Train Word2Vec on Wikipedia text (use gensim datasets)
- Find the 5 most similar words to: "doctor", "happy", "technology"
- Implement analogical reasoning: "Japan : Tokyo :: France : ?"

---

### Day 17 — The Attention Mechanism & Transformers

#### 🧠 Theory
- The problem with RNNs: sequential processing, limited context
- Attention: "which words matter most for this prediction?"
- Self-Attention: Q, K, V matrices (Query, Key, Value)
- Multi-Head Attention: attending to different aspects simultaneously
- Positional Encoding: handling sequence order without recurrence
- The Transformer architecture: Encoder and Decoder stacks

#### 💡 Example
```
Sentence: "The animal didn't cross the street because IT was too tired"

Self-Attention asks: What does "IT" refer to?
→ Attention score: "animal" = 0.9, "street" = 0.1

Multi-Head Attention:
Head 1: focuses on syntactic relationships
Head 2: focuses on semantic meaning
Head 3: focuses on coreference (what "IT" means)
```

#### 🛠️ Hands-On
```python
import numpy as np

def softmax(x): 
    return np.exp(x) / np.exp(x).sum(axis=-1, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)  # scale by sqrt(d_k)
    weights = softmax(scores)          # attention weights
    output = weights @ V               # weighted sum
    return output, weights

# Simulate attention for 3 tokens, 4-dim embeddings
np.random.seed(42)
Q = np.random.randn(3, 4)  # 3 tokens, 4-dim queries
K = np.random.randn(3, 4)  # 3 tokens, 4-dim keys  
V = np.random.randn(3, 4)  # 3 tokens, 4-dim values

output, attention_weights = scaled_dot_product_attention(Q, K, V)
print("Attention Weights:\n", attention_weights.round(3))
print("\nOutput shape:", output.shape)

# Visualize attention
import matplotlib.pyplot as plt
tokens = ['The', 'cat', 'sat']
plt.figure(figsize=(6, 5))
plt.imshow(attention_weights, cmap='Blues')
plt.xticks(range(3), tokens); plt.yticks(range(3), tokens)
plt.colorbar(); plt.title('Attention Weights')
for i in range(3):
    for j in range(3):
        plt.text(j, i, f'{attention_weights[i,j]:.2f}', ha='center', va='center')
plt.show()
```

#### 📝 Exercise
- Implement Multi-Head Attention from scratch (2 heads)
- Visualize attention patterns for different sentences
- Read the "Attention Is All You Need" paper abstract and summarize in your own words

---

### Day 18 — BERT & Pre-trained Language Models

#### 🧠 Theory
- BERT: Bidirectional Encoder Representations from Transformers
- Pre-training tasks: Masked Language Modeling, Next Sentence Prediction
- Fine-tuning BERT for downstream tasks
- The HuggingFace ecosystem: transformers, datasets, tokenizers
- Variants: RoBERTa, DistilBERT, ALBERT, XLNet

#### 💡 Example
```
BERT Training:
Input: "The [MASK] is the capital of France"
BERT predicts → "Paris"

This forces BERT to understand context from BOTH directions
(unlike GPT which only looks left-to-right)

Fine-tuning:
Pretrained BERT weights + small task-specific head
→ Sentiment Analysis, NER, Q&A, Text Classification
```

#### 🛠️ Hands-On
```python
from transformers import pipeline, AutoTokenizer, AutoModel
import torch

# Zero-shot classification (no training needed!)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
result = classifier(
    "This movie has stunning visuals and an incredible soundtrack",
    candidate_labels=["entertainment", "technology", "sports", "politics"]
)
print("Label:", result['labels'][0], "Score:", result['scores'][0])

# Sentiment Analysis
sentiment = pipeline("sentiment-analysis")
texts = ["I absolutely loved this product!", "Terrible experience, waste of money"]
for text, res in zip(texts, sentiment(texts)):
    print(f"'{text}' → {res['label']} ({res['score']:.3f})")

# Named Entity Recognition
ner = pipeline("ner", grouped_entities=True)
result = ner("Apple CEO Tim Cook announced new products in Cupertino, California")
for entity in result:
    print(f"{entity['entity_group']}: {entity['word']}")

# Feature extraction (embeddings)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello, how are you?", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
embeddings = outputs.last_hidden_state.mean(dim=1)
print("\nSentence embedding shape:", embeddings.shape)  # [1, 768]
```

#### 📝 Exercise
- Fine-tune DistilBERT on the IMDB sentiment dataset
- Compare DistilBERT vs TF-IDF + Logistic Regression (accuracy and speed)
- Run NER on 5 news headlines and analyze the results

---

### Day 19 — GPT & Generative Language Models

#### 🧠 Theory
- GPT vs BERT: decoder-only vs encoder-only architectures
- Autoregressive generation: predicting one token at a time
- Temperature, Top-K, Top-P sampling: controlling creativity
- Prompt engineering basics: zero-shot, few-shot, chain-of-thought
- GPT-2, GPT-3, GPT-4: scaling laws

#### 💡 Example
```
Temperature = 0.1 → Very focused, repetitive, conservative
Temperature = 1.0 → Balanced, natural
Temperature = 2.0 → Very creative, random, sometimes incoherent

Top-P = 0.9 → Sample from tokens covering 90% of probability mass
(only use high-probability tokens — cuts off unlikely completions)

Few-shot prompt:
"Positive: Great movie! → Happy
Negative: Awful film. → Sad
Neutral: It was fine. → "  ← GPT completes this
```

#### 🛠️ Hands-On
```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_text(prompt, max_length=100, temperature=0.8, top_p=0.9):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test different temperatures
prompt = "Artificial intelligence is transforming"
print("=== Temperature: 0.3 (Conservative) ===")
print(generate_text(prompt, temperature=0.3))

print("\n=== Temperature: 1.0 (Balanced) ===")
print(generate_text(prompt, temperature=1.0))

print("\n=== Temperature: 1.5 (Creative) ===")
print(generate_text(prompt, temperature=1.5))
```

#### 📝 Exercise
- Generate product descriptions for 5 different items using GPT-2
- Experiment with Top-K vs Top-P sampling
- Write 3 effective prompts using zero-shot, one-shot, and few-shot techniques

---

### Day 20 — Prompt Engineering

#### 🧠 Theory
- What is prompt engineering and why it matters
- Zero-shot, one-shot, few-shot prompting
- Chain-of-thought (CoT) prompting for reasoning
- System prompts and role-based prompting
- Prompt patterns: RPTQ (Role, Prompt, Task, Quality constraint)
- Common mistakes and how to avoid them

#### 💡 Example
```
BAD PROMPT: "Summarize this"
GOOD PROMPT: "You are an expert technical writer. Summarize the following 
research paper in 3 bullet points for a non-technical audience. 
Focus on: what problem it solves, the method used, and key results."

CHAIN-OF-THOUGHT:
"Solve step by step: If a train leaves at 3 PM traveling 60 mph 
and another leaves at 5 PM at 90 mph, when do they meet? 
Let me think through this step by step..."
```

#### 🛠️ Hands-On
```python
import anthropic  # or use openai

# Simulated prompt engineering examples
prompts = {
    "zero_shot": "What is quantum computing?",
    
    "few_shot": """Classify the sentiment:
    
    Input: "I love this product!"
    Output: Positive
    
    Input: "Worst purchase ever"
    Output: Negative
    
    Input: "It's okay, nothing special"
    Output: """,
    
    "chain_of_thought": """Problem: A store has 24 apples. They sell 1/3 in the morning 
    and 1/4 of the remaining in the afternoon. How many are left?
    
    Let's think step by step:
    Step 1: Calculate morning sales
    Step 2: Find remaining after morning
    Step 3: Calculate afternoon sales
    Step 4: Find final count""",
    
    "role_based": """You are an expert Python developer with 20 years of experience.
    Review this code and provide: 1) bugs, 2) performance issues, 3) style improvements.
    Be specific and provide corrected code for each issue.
    
    Code: def cal_avg(lst): return sum(lst)/len(lst)"""
}

for prompt_type, prompt in prompts.items():
    print(f"\n{'='*50}")
    print(f"PROMPT TYPE: {prompt_type.upper()}")
    print(f"PROMPT:\n{prompt}")
```

#### 📝 Exercise
- Write 5 prompts for the same task using different techniques
- Design a prompt template for an automated customer support system
- Test your prompts and document which one performs best and why

---

### Day 21 — 🏆 WEEK 3 MINI PROJECT: NLP Chatbot

#### Project: Intelligent FAQ Chatbot with Semantic Search

```python
# WEEK 3 MINI PROJECT — Semantic FAQ Chatbot
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Knowledge base
faq = {
    "What is your return policy?": "We offer 30-day returns for all items in original condition.",
    "How long does shipping take?": "Standard shipping takes 5-7 business days. Express is 2-3 days.",
    "Do you offer international shipping?": "Yes, we ship to 50+ countries. International orders take 10-15 days.",
    "How can I track my order?": "Use your order ID on our tracking page or check your email confirmation.",
    "What payment methods do you accept?": "We accept Visa, Mastercard, PayPal, and Apple Pay.",
    "How do I cancel an order?": "Orders can be cancelled within 24 hours of placement via your account page."
}

# Load semantic similarity model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode all FAQ questions
questions = list(faq.keys())
question_embeddings = model.encode(questions)

def get_answer(user_query, threshold=0.4):
    query_embedding = model.encode([user_query])
    similarities = cosine_similarity(query_embedding, question_embeddings)[0]
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]
    
    if best_score < threshold:
        return "I'm not sure about that. Please contact support@example.com", best_score
    
    return faq[questions[best_idx]], best_score

# Test the chatbot
test_queries = [
    "Can I return something?",
    "How fast will I get my package?",
    "Do you ship overseas?",
    "What's the price of item 123?"
]

print("=" * 60)
print("🤖 FAQ CHATBOT — Semantic Search Powered")
print("=" * 60)

for query in test_queries:
    answer, score = get_answer(query)
    print(f"\n👤 User: {query}")
    print(f"🤖 Bot: {answer}")
    print(f"   [Confidence: {score:.3f}]")

# Interactive loop
print("\n" + "="*60)
print("Interactive mode (type 'quit' to exit)")
while True:
    user_input = input("\n👤 You: ").strip()
    if user_input.lower() == 'quit': break
    answer, score = get_answer(user_input)
    print(f"🤖 Bot: {answer} [Confidence: {score:.3f}]")
```

**Deliverables:**
- [ ] FAQ knowledge base (minimum 10 Q&A pairs)
- [ ] Semantic similarity using sentence-transformers
- [ ] Confidence thresholding
- [ ] Interactive chatbot loop
- [ ] Evaluation: test 20 paraphrased questions

---

## 📅 WEEK 4 — Generative AI, LLMs & Production
> **Theme:** Diffusion models, LLM APIs, RAG, fine-tuning, and deploying AI to production.

---

### Day 22 — Introduction to Generative AI & Diffusion Models

#### 🧠 Theory
- What makes AI "generative": creating new data vs classifying
- Generative Adversarial Networks (GANs): Generator vs Discriminator
- Variational Autoencoders (VAEs): latent space and sampling
- Diffusion Models: how DALL-E, Stable Diffusion, Midjourney work
- Forward diffusion (add noise) vs Reverse diffusion (denoise)
- Text-to-image pipeline: CLIP + Diffusion

#### 💡 Example
```
Diffusion Model Training:
1. Take a clear cat photo
2. Gradually add Gaussian noise (step 1 to step 1000)
3. Train model to REVERSE this process
4. At inference: start from pure noise → run reverse 1000 steps → cat photo!

Why it works: The model learns the "probability distribution" of all cats
Then samples a NEW cat from that distribution
```

#### 🛠️ Hands-On
```python
# Simple GAN to understand the Generator/Discriminator concept
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# Generator: noise → fake data
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(16, 64), nn.ReLU(),
            nn.Linear(64, 128), nn.ReLU(),
            nn.Linear(128, 2)  # generates 2D points
        )
    def forward(self, z): return self.net(z)

# Discriminator: data → real or fake
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64), nn.LeakyReLU(0.2),
            nn.Linear(64, 32), nn.LeakyReLU(0.2),
            nn.Linear(32, 1), nn.Sigmoid()
        )
    def forward(self, x): return self.net(x)

G = Generator(); D = Discriminator()
optG = torch.optim.Adam(G.parameters(), lr=2e-4)
optD = torch.optim.Adam(D.parameters(), lr=2e-4)
criterion = nn.BCELoss()

# Real data: points from a circle
def real_data(n): 
    theta = torch.rand(n) * 2 * np.pi
    r = 2 + 0.3 * torch.randn(n)
    return torch.stack([r * torch.cos(theta), r * torch.sin(theta)], dim=1)

# Training loop
for epoch in range(2000):
    real = real_data(64)
    noise = torch.randn(64, 16)
    fake = G(noise)
    
    # Train D
    optD.zero_grad()
    loss_D = criterion(D(real), torch.ones(64,1)) + criterion(D(fake.detach()), torch.zeros(64,1))
    loss_D.backward(); optD.step()
    
    # Train G
    optG.zero_grad()
    loss_G = criterion(D(fake), torch.ones(64,1))
    loss_G.backward(); optG.step()

# Visualize
with torch.no_grad():
    fake_pts = G(torch.randn(200, 16)).numpy()
    real_pts = real_data(200).numpy()

plt.figure(figsize=(10, 4))
plt.subplot(1,2,1); plt.scatter(*real_pts.T, s=5); plt.title('Real Data')
plt.subplot(1,2,2); plt.scatter(*fake_pts.T, s=5, c='red'); plt.title('GAN Generated')
plt.show()
```

#### 📝 Exercise
- Experiment with DALL-E or Stable Diffusion API to generate images
- Describe the 5 best prompts you found for high-quality image generation
- What is "prompt injection" in image generation and how do you avoid it?

---

### Day 23 — Working with LLM APIs

#### 🧠 Theory
- OpenAI API vs Anthropic Claude API vs Google Gemini
- API structure: system prompts, user messages, assistant responses
- Token counting and cost optimization
- Streaming responses for real-time UX
- Function calling / Tool use
- Rate limits, retries, and error handling

#### 💡 Example
```python
# System prompt = personality and constraints
# User message = current request
# Assistant = previous responses (conversation history)

messages = [
    {"role": "system", "content": "You are a helpful Python tutor. Explain clearly."},
    {"role": "user", "content": "What is a decorator?"},
    {"role": "assistant", "content": "A decorator is..."},
    {"role": "user", "content": "Show me an example"}  # multi-turn!
]
```

#### 🛠️ Hands-On
```python
# OpenAI API Example
from openai import OpenAI
import json

client = OpenAI()  # uses OPENAI_API_KEY env variable

# Basic completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI/ML tutor. Be concise."},
        {"role": "user", "content": "Explain gradient descent in 3 sentences"}
    ],
    temperature=0.7,
    max_tokens=200
)
print(response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")

# Function Calling (Tool Use)
tools = [{
    "type": "function",
    "function": {
        "name": "get_stock_price",
        "description": "Get the current stock price for a given symbol",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Stock ticker (e.g., AAPL)"}
            },
            "required": ["symbol"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's Apple's stock price?"}],
    tools=tools,
    tool_choice="auto"
)

# Check if model wants to call a function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    print(f"Tool requested: {tool_call.function.name}({args})")

# Streaming
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a haiku about AI"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
```

#### 📝 Exercise
- Build a multi-turn conversation that remembers context
- Implement a retry mechanism with exponential backoff
- Calculate the cost of running 1000 API calls with different models

---

### Day 24 — Retrieval-Augmented Generation (RAG)

#### 🧠 Theory
- Why LLMs hallucinate: they only know their training data
- RAG = LLM + External Knowledge Database
- Vector databases: what they are, how they work (FAISS, ChromaDB, Pinecone)
- Embeddings for semantic search
- The RAG pipeline: Index → Retrieve → Augment → Generate
- Advanced RAG: re-ranking, hybrid search, chunking strategies

#### 💡 Example
```
Without RAG: "What is our Q3 revenue?" → LLM guesses or halluccinates
With RAG:
1. Convert all company docs to embeddings → vector DB
2. Query: "Q3 revenue" → find similar doc chunks
3. Inject found chunks into prompt
4. LLM generates answer BASED ON real company data

RAG = Long-term memory for LLMs
```

#### 🛠️ Hands-On
```python
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import faiss  # pip install faiss-cpu

# Simulate a RAG system without API key
encoder = SentenceTransformer('all-MiniLM-L6-v2')

# Knowledge base (simulate company docs)
documents = [
    "Our Q3 2024 revenue was $2.4 billion, up 15% year-over-year",
    "The new product launch is scheduled for March 15, 2025",
    "Customer satisfaction score hit 4.8/5 in Q3 2024",
    "We have 2,400 employees across 12 offices globally",
    "Python and React are our primary technology stacks",
    "The company was founded in 2018 by Sarah Chen and Michael Park",
    "Annual recurring revenue grew to $850M in 2024",
    "We operate in North America, Europe, and APAC regions"
]

# Step 1: Create embeddings and index
doc_embeddings = encoder.encode(documents)

# Build FAISS index
dim = doc_embeddings.shape[1]
index = faiss.IndexFlatIP(dim)  # Inner product (cosine similarity)
# Normalize for cosine similarity
faiss.normalize_L2(doc_embeddings)
index.add(doc_embeddings.astype('float32'))

def retrieve(query, top_k=3):
    query_embedding = encoder.encode([query])
    faiss.normalize_L2(query_embedding)
    distances, indices = index.search(query_embedding.astype('float32'), top_k)
    
    results = []
    for idx, score in zip(indices[0], distances[0]):
        results.append({'document': documents[idx], 'score': score})
    return results

def rag_answer(query):
    print(f"\n❓ Query: {query}")
    chunks = retrieve(query)
    
    context = "\n".join([f"- {r['document']}" for r in chunks])
    print(f"\n📚 Retrieved context:\n{context}")
    
    prompt = f"""Based on the following company information, answer the question.
    
Context:
{context}

Question: {query}

Answer based ONLY on the provided context:"""
    
    print(f"\n💬 (Send this prompt to LLM for final answer)")
    return prompt

rag_answer("What was our revenue last quarter?")
rag_answer("Who founded the company?")
```

#### 📝 Exercise
- Build a RAG system for a set of Wikipedia articles
- Implement chunking: split documents into 200-word chunks with 50-word overlap
- Compare RAG vs direct LLM: which is more accurate on your docs?

---

### Day 25 — Fine-tuning LLMs

#### 🧠 Theory
- When to fine-tune vs prompt engineer vs RAG
- Full fine-tuning vs parameter-efficient fine-tuning (PEFT)
- LoRA (Low-Rank Adaptation): training only small adapter layers
- QLoRA: quantized LoRA for consumer GPUs
- RLHF: Reinforcement Learning from Human Feedback (how ChatGPT was trained)
- Dataset formats for fine-tuning: instruction datasets, JSONL format

#### 💡 Example
```
Full Fine-tuning: Train all 7 billion parameters (requires 8x A100 GPUs)
LoRA: Add small matrices (rank 8-64) to attention layers
      Only train ~1% of parameters → same GPU as inference!

RLHF Pipeline:
1. Supervised Fine-tuning (SFT): train on human-written responses
2. Reward Model: train to score response quality
3. PPO: optimize LLM to maximize reward model score
```

#### 🛠️ Hands-On
```python
# LoRA Fine-tuning with Hugging Face (conceptual - needs GPU)
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType
from datasets import Dataset
import torch

# Configure LoRA
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,              # rank of LoRA matrices (smaller = fewer params)
    lora_alpha=32,     # scaling factor
    target_modules=["q_proj", "v_proj"],  # which layers to adapt
    lora_dropout=0.1,
    bias="none"
)

# Load model (using small model for demo)
model_name = "microsoft/phi-2"  # 2.7B parameter model
tokenizer = AutoTokenizer.from_pretrained(model_name)

# In practice with GPU:
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
# model = get_peft_model(model, lora_config)
# model.print_trainable_parameters()
# → trainable params: 1,720,320 || all params: 2,779,750,400 || trainable%: 0.062%

# Prepare instruction dataset
data = [
    {"instruction": "Classify sentiment", "input": "I love this!", "output": "Positive"},
    {"instruction": "Classify sentiment", "input": "Terrible product", "output": "Negative"},
]

def format_instruction(sample):
    return f"""### Instruction: {sample['instruction']}
### Input: {sample['input']}
### Response: {sample['output']}"""

print("Example training format:")
print(format_instruction(data[0]))
print("\nLoRA config summary:")
print(f"Rank: {lora_config.r}")
print(f"Target modules: {lora_config.target_modules}")
print(f"Approximate parameter reduction: ~99%")
```

#### 📝 Exercise
- Prepare a fine-tuning dataset (50 examples) in instruction format for a specific task
- Compare: zero-shot vs few-shot vs fine-tuned model performance
- Research: What datasets were used to fine-tune Llama 2?

---

### Day 26 — LangChain & AI Agents

#### 🧠 Theory
- What is LangChain: orchestration framework for LLM apps
- Chains: sequence of LLM calls and operations
- Agents: LLMs that autonomously decide which tools to use
- Tools: web search, code execution, calculators, APIs
- Memory: conversation memory types (buffer, summary, vector)
- ReAct framework: Reason + Act loop

#### 💡 Example
```
AI Agent for Research Task:
User: "What are the top 5 AI papers in 2024 and summarize them?"

Agent thinks (ReAct loop):
Thought: I need to search for recent AI papers
Action: web_search("top AI papers 2024")
Observation: [search results]
Thought: I should read the top 3 results in full
Action: web_fetch(url1), web_fetch(url2), web_fetch(url3)
Thought: Now I can summarize
Action: final_answer(summary)
```

#### 🛠️ Hands-On
```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

# Basic Chain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate.from_template(
    "You are an expert in {subject}. Explain {topic} in simple terms."
)

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(subject="Machine Learning", topic="gradient descent")
print(result)

# Memory-enabled conversation
memory = ConversationBufferMemory(return_messages=True)

# Agent with tools
def calculate(expression):
    """Evaluate mathematical expressions"""
    try: return str(eval(expression))
    except: return "Invalid expression"

tools = [
    Tool(name="Calculator", func=calculate, 
         description="For math calculations. Input: math expression like '2+2'"),
]

agent = initialize_agent(
    tools=tools, llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory, verbose=True
)

agent.run("What is 15% of 340?")
```

#### 📝 Exercise
- Build a LangChain pipeline that: reads a PDF → summarizes → answers questions
- Create an agent with 3 tools: calculator, current time, and word counter
- Implement conversation memory that summarizes old messages automatically

---

### Day 27 — Deploying AI Models to Production

#### 🧠 Theory
- Model serving: REST APIs with FastAPI, Flask
- Docker containers for ML models
- Cloud deployment: AWS SageMaker, Google Vertex AI, Azure ML, HuggingFace Spaces
- Model monitoring: data drift, concept drift, performance degradation
- A/B testing for models
- Latency optimization: quantization, batching, caching

#### 💡 Example
```
Production ML Stack:
FastAPI (serving) → Docker (packaging) → Kubernetes (scaling)
→ Prometheus + Grafana (monitoring) → MLflow (experiment tracking)

Response time benchmarks:
- P50: 50% of requests served in < X ms
- P95: 95% of requests served in < X ms  
- P99: 99% of requests served in < X ms
```

#### 🛠️ Hands-On
```python
# FastAPI ML Model Serving
# requirements: pip install fastapi uvicorn scikit-learn joblib pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List
import time

app = FastAPI(title="ML Model API", description="Churn Prediction API", version="1.0")

# Request/Response schemas
class PredictionRequest(BaseModel):
    tenure: float
    monthly_charges: float
    total_charges: float
    contract_type: str  # "Month-to-month", "One year", "Two year"

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    churn_risk: str
    response_time_ms: float

# Simulate a loaded model
from sklearn.ensemble import RandomForestClassifier
demo_model = RandomForestClassifier(n_estimators=10)
# In production: model = joblib.load("model.pkl")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "churn-predictor-v1"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    start = time.time()
    try:
        contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
        features = np.array([[
            request.tenure,
            request.monthly_charges,
            request.total_charges,
            contract_map.get(request.contract_type, 0)
        ]])
        
        # Simulate prediction
        probability = float(np.random.random())
        prediction = int(probability > 0.5)
        risk = "High" if probability > 0.7 else "Medium" if probability > 0.4 else "Low"
        
        return PredictionResponse(
            prediction=prediction,
            probability=round(probability, 4),
            churn_risk=risk,
            response_time_ms=round((time.time() - start) * 1000, 2)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Dockerfile content:
print("""
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Run: docker build -t churn-api . && docker run -p 8000:8000 churn-api
# Test: curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" 
#        -d '{"tenure": 24, "monthly_charges": 65.5, "total_charges": 1572, "contract_type": "Month-to-month"}'
""")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 📝 Exercise
- Dockerize your Week 1 churn prediction model
- Add input validation (Pydantic) and error handling
- Implement a /batch endpoint that accepts multiple predictions

---

### Day 28 — AI Ethics, Safety & Responsible AI

#### 🧠 Theory
- Bias in AI: sources, types, and real-world harm
- Fairness metrics: demographic parity, equalized odds, individual fairness
- Explainable AI (XAI): LIME, SHAP
- AI Safety: alignment, hallucination, adversarial attacks
- Data privacy: differential privacy, federated learning
- AI regulations: EU AI Act, GDPR implications

#### 💡 Example
```
Amazon's Hiring AI (2018):
→ Trained on 10 years of résumés (mostly male engineers)
→ Learned to penalize résumés containing "women's"
→ Penalized graduates of all-women's colleges
→ Amazon shut it down

Lesson: Biased training data → biased model → real-world harm

SHAP explanation: "This loan was DENIED because:
  - Low income (-0.35 impact)
  - High debt ratio (-0.28 impact)  
  - Short credit history (-0.19 impact)"
```

#### 🛠️ Hands-On
```python
import shap
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer

# Load and train model
data = load_breast_cancer()
X, y = pd.DataFrame(data.data, columns=data.feature_names), data.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingClassifier(n_estimators=100)
model.fit(X_train, y_train)

# SHAP Explanations
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Global feature importance
shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)

# Individual prediction explanation
shap.force_plot(
    explainer.expected_value,
    shap_values[0],
    X_test.iloc[0],
    show=False
)

print("Top 5 most important features (SHAP):")
mean_shap = np.abs(shap_values).mean(0)
feature_importance = pd.Series(mean_shap, index=data.feature_names).sort_values(ascending=False)
print(feature_importance[:5])

# Fairness check (demo)
def check_demographic_parity(predictions, sensitive_attr):
    for group in sensitive_attr.unique():
        group_mask = sensitive_attr == group
        approval_rate = predictions[group_mask].mean()
        print(f"Group {group}: {approval_rate:.3f} approval rate")
```

#### 📝 Exercise
- Apply SHAP to your Week 1 churn prediction model
- Identify if your model is biased by gender or age in the Titanic dataset
- Write a 1-page "Model Card" for your best model (purpose, limitations, bias, usage)

---

### Day 29 — MLOps & Experiment Tracking

#### 🧠 Theory
- MLOps: DevOps for Machine Learning
- Experiment tracking with MLflow, Weights & Biases
- Model versioning and registry
- CI/CD for ML: automated testing and deployment
- Data versioning with DVC
- Feature stores

#### 💡 Example
```
Without MLOps: "Which model was that? I ran 47 experiments last week..."
With MLOps:
- Every experiment logs: params, metrics, code version, dataset hash
- Best model promoted to Registry → Staging → Production
- Automatic alerts if production accuracy drops

CI/CD Pipeline for ML:
Code commit → Unit tests → Integration tests → 
Model training → Validation → Docker build → Deploy → Monitor
```

#### 🛠️ Hands-On
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

# Load data
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_experiment("breast-cancer-classification")

# Experiment 1: Random Forest
params_list = [
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 100, "max_depth": 5},
    {"n_estimators": 200, "max_depth": 7},
]

for params in params_list:
    with mlflow.start_run(run_name=f"RF_n{params['n_estimators']}_d{params['max_depth']}"):
        # Log parameters
        mlflow.log_params(params)
        
        # Train
        model = RandomForestClassifier(**params, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
        
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_prob)
        }
        
        # Log metrics and model
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Params: {params} → Accuracy: {metrics['accuracy']:.4f}")

print("\n✅ All experiments logged! Run 'mlflow ui' to view the dashboard.")
```

#### 📝 Exercise
- Set up MLflow tracking for your Week 2 CNN experiment
- Compare 10 different hyperparameter combinations and pick the best
- Set up a simple CI/CD pipeline using GitHub Actions for model testing

---

### Day 30 — 🏆 WEEK 4 FINAL PROJECT: Full-Stack AI Application

#### Project: AI-Powered Job Application Assistant

**Architecture:**
```
User → FastAPI Backend → RAG System → LLM API
                       ↓
                  Resume Parser + Vector DB
```

```python
# FINAL PROJECT — AI Job Application Assistant
# Full stack: FastAPI + RAG + LLM + Embeddings

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Optional
import re

app = FastAPI(title="AI Job Application Assistant")
encoder = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory knowledge base
resume_knowledge = []
resume_embeddings = None

class JobAnalysisRequest(BaseModel):
    job_description: str
    custom_question: Optional[str] = None

class ResumeMatch(BaseModel):
    match_score: float
    matching_skills: List[str]
    missing_skills: List[str]
    improvement_suggestions: List[str]
    cover_letter_draft: str

def extract_skills(text: str) -> List[str]:
    """Extract tech skills from text"""
    skill_patterns = [
        'python', 'java', 'javascript', 'react', 'sql', 'machine learning',
        'deep learning', 'tensorflow', 'pytorch', 'aws', 'docker', 'kubernetes',
        'nlp', 'computer vision', 'fastapi', 'data science', 'pandas', 'numpy'
    ]
    found = [s for s in skill_patterns if s.lower() in text.lower()]
    return found

def cosine_similarity_score(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    global resume_knowledge, resume_embeddings
    content = await file.read()
    resume_text = content.decode('utf-8', errors='ignore')
    
    # Chunk the resume
    sentences = [s.strip() for s in resume_text.split('.') if len(s.strip()) > 20]
    resume_knowledge = sentences
    resume_embeddings = encoder.encode(sentences)
    
    return {"message": f"Resume loaded: {len(sentences)} sections indexed", "skills": extract_skills(resume_text)}

@app.post("/analyze-job-fit", response_model=ResumeMatch)
async def analyze_job_fit(request: JobAnalysisRequest):
    if not resume_knowledge:
        return ResumeMatch(
            match_score=0, matching_skills=[], missing_skills=[],
            improvement_suggestions=["Please upload your resume first"],
            cover_letter_draft="Please upload your resume to generate a cover letter."
        )
    
    jd = request.job_description
    jd_embedding = encoder.encode([jd])[0]
    
    # Find matching resume sections
    similarities = [cosine_similarity_score(jd_embedding, re) for re in resume_embeddings]
    top_k = sorted(enumerate(similarities), key=lambda x: -x[1])[:3]
    best_sections = [resume_knowledge[i] for i, _ in top_k]
    
    # Skill gap analysis
    jd_skills = extract_skills(jd)
    resume_all_text = ' '.join(resume_knowledge)
    resume_skills = extract_skills(resume_all_text)
    
    matching = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    match_score = len(matching) / max(len(jd_skills), 1)
    
    # Generate improvement suggestions
    suggestions = []
    if missing: suggestions.append(f"Highlight or acquire: {', '.join(missing)}")
    if match_score < 0.6: suggestions.append("Consider tailoring your resume to include more JD keywords")
    if len(resume_knowledge) < 10: suggestions.append("Expand your resume with more detail")
    
    # Draft cover letter (template — replace with LLM call in production)
    cover_letter = f"""Dear Hiring Manager,

I am excited to apply for this position. Based on the job requirements, 
my background in {', '.join(matching[:3]) if matching else 'relevant technologies'} 
aligns strongly with your needs.

{best_sections[0] if best_sections else 'My experience demonstrates strong relevant skills.'}

I am eager to contribute my expertise and grow within your team.

Best regards,
[Your Name]"""
    
    return ResumeMatch(
        match_score=round(match_score * 100, 1),
        matching_skills=matching,
        missing_skills=missing,
        improvement_suggestions=suggestions,
        cover_letter_draft=cover_letter
    )

@app.get("/")
def root():
    return {
        "endpoints": {
            "POST /upload-resume": "Upload resume (text file)",
            "POST /analyze-job-fit": "Get match analysis and cover letter",
            "GET /health": "API health check"
        }
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 AI Job Application Assistant running on http://localhost:8000")
    print("📚 Docs available at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Deliverables:**
- [ ] Resume upload and parsing
- [ ] RAG-based job description matching
- [ ] Skill gap analysis
- [ ] Cover letter generation using LLM API
- [ ] REST API with documentation (FastAPI auto-docs)
- [ ] Docker deployment
- [ ] Demo with 3 different job descriptions

---

## 📊 30-Day Progress Tracker

| Week | Days | Focus Area | Skills Acquired | Project |
|------|------|-----------|-----------------|---------|
| 1 | 1-7 | ML Foundations | Python, NumPy, Pandas, sklearn, Linear/Logistic Regression, Decision Trees | Churn Prediction |
| 2 | 8-14 | Advanced ML + DL | Ensembles, CNNs, LSTMs, TensorFlow, Transfer Learning | Image Classifier |
| 3 | 15-21 | NLP + Transformers | BERT, GPT, Embeddings, Prompt Engineering, LangChain | Semantic Chatbot |
| 4 | 22-30 | Gen-AI + Production | RAG, Fine-tuning, FastAPI, MLOps, Ethics, Deployment | AI Job Assistant |

---

## 🛠️ Essential Tools & Technologies

| Category | Tools |
|----------|-------|
| **Python Core** | NumPy, Pandas, Matplotlib, Seaborn |
| **Classical ML** | Scikit-learn, XGBoost, LightGBM |
| **Deep Learning** | TensorFlow/Keras, PyTorch |
| **NLP/LLMs** | HuggingFace Transformers, NLTK, spaCy, Gensim |
| **Gen-AI** | OpenAI API, Anthropic API, LangChain |
| **Vector DBs** | FAISS, ChromaDB, Pinecone |
| **MLOps** | MLflow, Weights & Biases, DVC |
| **Deployment** | FastAPI, Docker, uvicorn |
| **Cloud** | AWS SageMaker / Google Vertex AI / HuggingFace Spaces |

---

## 📚 Learning Resources

- **Books:** "Hands-On ML with Scikit-Learn, Keras & TensorFlow" (Aurélien Géron)
- **Papers:** "Attention Is All You Need", "BERT", "GPT-3" (available on arxiv.org)
- **Courses:** fast.ai, DeepLearning.AI on Coursera
- **Practice:** Kaggle competitions, HuggingFace daily papers
- **Communities:** r/MachineLearning, Papers With Code, HuggingFace Discord

---

## ✅ Daily Checklist Template

```markdown
### Day X — [Topic]
- [ ] Read theory (30 min)
- [ ] Study examples and analogies (15 min)
- [ ] Run hands-on code (45 min)
- [ ] Complete exercise (30 min)
- [ ] Write 3-bullet summary of what you learned
- [ ] Push code to GitHub
```

---

> 🎯 **Remember:** Consistency beats intensity. 2 hours daily is better than 14 hours once a week.
> The best project is one you finish. Start simple, iterate fast.
> 
> **You've got this. 30 days from now, you'll be building real AI systems.** 🚀
