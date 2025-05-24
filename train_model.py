# train_model.py
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# 🔧 Create folder to save trained model and features
os.makedirs('trained_data', exist_ok=True)

# 📥 Load dataset
df = pd.read_csv('csv/Students_Grading_Dataset_Biased.csv')

# 🧪 DEBUG: Check column names
print("CSV columns:", df.columns.tolist())

# ➕ Create binary target column 'Passed' based on Total_Score
if 'Passed' not in df.columns:
    df['Passed'] = df['Total_Score'].apply(lambda x: 1 if x >= 75 else 0)

# 🧹 Select input features and target
feature_columns = ['Sleep_Hours', 'Study_Hours', 'Participation_Score', 'Attendance']
X = df[feature_columns]
y = df['Passed']

# 📊 Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🧠 Create ML pipeline with imputation, scaling, and classification
cls_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),     # Fill missing values with column mean
    ('scaler', StandardScaler()),                    # Normalize inputs
    ('classifier', MLPClassifier(
        hidden_layer_sizes=(64,),                    # Single hidden layer with 64 neurons
        activation='logistic',                       # Sigmoid activation
        max_iter=2000,
        early_stopping=True,
        random_state=42
    ))
])

# 🚀 Train the model
cls_pipeline.fit(X_train, y_train)

# 💾 Save model and feature column names
joblib.dump(cls_pipeline, 'trained_data/student_pass_fail_model.pkl')
joblib.dump(feature_columns, 'trained_data/student_features.pkl')

print("✅ Training complete. Model saved.")
