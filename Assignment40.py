#Case Study - Student Peformance

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

#######################################################################
#######################################################################

print("Load the data...")

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

fea_Cols = [
    "Attendance",
    "PreviousScore"
]
X = df[fea_Cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)  #Split data in 4 parts #Split in size = train_size=0.5#random_state=42 - Shuffling
model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train,Y_train)


Y_Pred = model.predict(X_test)
print("Predicted value is :", Y_Pred)


accuracy = accuracy_score(Y_Pred,Y_test)
print(f"Accuracy of the result by : {accuracy*100}%")

#1
importance = model.feature_importances_
print("Importance feature of each column")
for col, score in zip(X.columns, importance):
    print(f"{col}: {score:.4f}")

#2
X_new = df.drop(columns=["SleepHours","FinalResult"])
Y_new = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X_new, Y_new, train_size=0.5, random_state=42)
model_new = DecisionTreeClassifier(max_depth=5)
model_new.fit(X_train, Y_train)

acc_new = accuracy_score(Y_test, model_new.predict(X_test))
print(f"New accuracy (without SleepHours): {acc_new * 100:.2f}%")

#3

X = df[["StudyHours", "Attendance"]]
Y = df["FinalResult"]

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.5, random_state=42)

# Train model
model_simple = DecisionTreeClassifier(max_depth=5)
model_simple.fit(X_train, Y_train)

acc_simple = accuracy_score(Y_test, model_simple.predict(X_test))
print(f"Accuracy (StudyHours + Attendance): {acc_simple * 100:.2f}%")


#4
new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 7, 8],
    "Attendance": [65, 75, 85, 90, 95]
})

predictions = model_simple.predict(new_students)
new_students["PredictedResult"] = predictions
print(new_students)


#5

Y_pred = model_simple.predict(X_test)
correct = sum(Y_pred == Y_test)
total = len(Y_test)
manual_accuracy = correct / total
print(f"Manual Accuracy: {manual_accuracy * 100:.2f}%")

#6

misclassified = X_test[Y_test != Y_pred]
print("Misclassified students:\n", misclassified)

count_misclassified = (Y_test != Y_pred).sum()
print(f"Number of misclassified students: {count_misclassified}")

#7
for state in [0, 10, 42]:
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.5, random_state=state)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, Y_train)
    acc = accuracy_score(Y_test, model.predict(X_test))
    print(f"Random state {state}: Testing Accuracy = {acc * 100:.2f}%")


#8

plt.figure(figsize=(10,6))
plot_tree(model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True)
plt.title("Decision Tree Visualization - Student Performance")
plt.show()


#9

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
X = df[["PerformanceIndex", "PreviousScore"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.5, random_state=42)
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, Y_train)
acc = accuracy_score(Y_test, model.predict(X_test))
print(f"Accuracy with PerformanceIndex: {acc * 100:.2f}%")


#10
model_full = DecisionTreeClassifier(max_depth=None)
model_full.fit(X_train, Y_train)

train_acc = accuracy_score(Y_train, model_full.predict(X_train))
test_acc = accuracy_score(Y_test, model_full.predict(X_test))

print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy: {test_acc * 100:.2f}%")

