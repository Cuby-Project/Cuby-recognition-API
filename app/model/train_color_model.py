import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
df = pd.read_csv('../../data/dataset.csv')
X = df[['H', 'S', 'V']].values
y = df['label'].values

# Train/test split (optional for validation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Save model
os.makedirs('', exist_ok=True)
joblib.dump(model, 'color_model.pkl')

print("✅ Model trained and saved to app/model/color_model.pkl")
