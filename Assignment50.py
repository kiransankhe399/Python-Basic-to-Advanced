#Breast Cancer Case Study Prediction using Decision Tree Classifier

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#------------------------------------------------------------------
# Step 1: Load the dataset
#------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")
print("Shape of the dataset:", df.shape)
print("First 5 rows of the dataset:")
print(df.head())
print("Dataset loaded successfully.")

#------------------------------------------------------------------
#Step 2: Seperate features and labels
#------------------------------------------------------------------

X = df.drop('target', axis=1)  # Features
Y = df['target']  # Labels

print("X Shape:", X.shape)  
print("Y Shape:", Y.shape) 

#------------------------------------------------------------------
#Step 3 : Split the dataset into training and testing sets
#------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("Training set shape:", X_train.shape, Y_train.shape)
print("Testing set shape:", X_test.shape, Y_test.shape)

#------------------------------------------------------------------
#Step 4 : Feature Scaling
#------------------------------------------------------------------

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
print("Feature scaling completed.")

#------------------------------------------------------------------
#Step 5 : Create the model and train it using Decision Tree Classifier
#------------------------------------------------------------------

model = DecisionTreeClassifier(random_state=42)

model = model.fit(X_train, Y_train)
print("Model training completed.")

#------------------------------------------------------------------
#Step 6 : Test the model 
#------------------------------------------------------------------

Y_pred = model.predict(X_test)
print("Testing of model completed.")

#------------------------------------------------------------------
#Step 7 : Evaluate the model
#------------------------------------------------------------------

print(f"Accuracy Score:", accuracy_score(Y_test, Y_pred)* 100, "%")

print("Confusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))


#------------------------------------------------------------------