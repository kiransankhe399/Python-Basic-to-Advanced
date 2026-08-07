#Case Study - Student Peformance

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.metrics import confusion_matrix
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

# 2
Y_Pred = model.predict(X_test)
print("Predicted value is :", Y_Pred)

# 3
accuracy = accuracy_score(Y_Pred,Y_test)
print(f"Accuracy of the result by : {accuracy*100}%")

# 4
cm = confusion_matrix(Y_test,Y_Pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap = "Blues")
plt.title("Confusion Matrix - Student Performance")
plt.show()

#5 
train_pred = model.predict(X_train)
accuracy = accuracy_score(Y_train,train_pred)
print(f"Accuracy of the training is : {accuracy*100}%")

test_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,test_pred)
print(f"Accuracy of the testing is : {accuracy*100}%")

#6

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)  #Split data in 4 parts #Split in size = train_size=0.5#random_state=42 - Shuffling
# Model 1: max_depth = 1
model1 = DecisionTreeClassifier(max_depth=1)
model1.fit(X_train, Y_train)
Y_Pred1 = model1.predict(X_test)
acc1 = accuracy_score(Y_test, Y_Pred1)
print(f"Accuracy (max_depth=1): {acc1 * 100:.2f}%")

# Model 2: max_depth = 3
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=52)  #Split data in 4 parts #Split in size = train_size=0.5#random_state=42 - Shuffling

model2 = DecisionTreeClassifier(max_depth=3)
model2.fit(X_train, Y_train)
Y_Pred2 = model2.predict(X_test)
acc2 = accuracy_score(Y_test, Y_Pred2)
print(f"Accuracy (max_depth=3): {acc2 * 100:.2f}%")

# Model 3: max_depth = None
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=48)  #Split data in 4 parts #Split in size = train_size=0.5#random_state=42 - Shuffling

model3 = DecisionTreeClassifier(max_depth=None)
model3.fit(X_train, Y_train)
Y_Pred3 = model3.predict(X_test)
acc3 = accuracy_score(Y_test, Y_Pred3)
print(f"Accuracy (max_depth=None): {acc3 * 100:.2f}%")

#7

new_student = [[6, 85, 66, 7, 7]]  
result = model.predict(new_student)

if result[0] == 1:
    print("The student will Pass ")
else:
    print("The student will Fail ")


