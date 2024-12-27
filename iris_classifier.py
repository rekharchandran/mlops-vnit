# -*- coding: utf-8 -*-
"""Iris classifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tKViKplTPKHdTAZr6FKpLB-wQw3gn22T
"""

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (Setosa, Versicolor, Virginica)

# Convert to DataFrame for easier analysis
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['target'] = y

# Map target labels to their species names
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Perform cross-validation
model = LogisticRegression(max_iter=200)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')  # 5-fold cross-validation

print("\nCross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Logistic Regression model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy on Test Set:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Optional: Test with new data
sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Replace with your own values
prediction = model.predict(sample)
predicted_species = iris.target_names[prediction[0]]
print("\nPrediction for sample {}: {}".format(sample, predicted_species))
