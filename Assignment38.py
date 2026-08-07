#Case Study - Student Peformance

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#######################################################################
#Question 1 :
#######################################################################

print("Load the data...")

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print(f"First 5 record from : {DataPath} are...")
print(df.head())

print(f"Last 5 record from : {DataPath} are...")
print(df.tail())

print(f"Total number of rows and columns are...")
count = 0
row = len(df)
for c in df.columns:
    count  = count + 1
print(f"Total number of columns is :{count}, and Total number of row is : {row}")

print(f"List of columns are...")
for c in df.columns:
    print(c)

print(f"Datatype of columns are...")
print(f"DataType is :{df.dtypes}")


#######################################################################
#Question 2
#######################################################################

print(f"Total number of students : {row}") 

countPass = 0
countFail = 0
for std in df["FinalResult"]:
    if std == 1:
        countPass = countPass +1
    else:
        countFail = countFail + 1

print(f"Total Student pass is : {countPass}")
print(f"Total Student Fail is : {countFail}")

#######################################################################
#Question 3
#######################################################################

print(f"Average study hours is : {df["StudyHours"].mean()}")

print(f"Average Attendance is : {df["Attendance"].mean()}")

maxScore = []
for shr in df["PreviousScore"]:
    maxScore.append(shr)
max(maxScore)
print(f"Max Previous Score is : {max(maxScore)}")

minSleep = []
for shr in df["SleepHours"]:
    minSleep.append(shr)
print(f"Minimum Sleep is : {min(minSleep)}")

#######################################################################
#Question 4
#######################################################################

print("Class Distribution (FinalResult)")
print(df["FinalResult"].value_counts())

percentPass = (countPass/ (countPass + countFail)) * 100
print(f"Percentage of Pass student : {percentPass}%")

percentFail = (countFail/ (countPass + countFail)) * 100
print(f"Percentage of Fail student : {percentFail}%")


#######################################################################
#Question 5
#######################################################################

fea_Cols = [
    "StudyHours",
    "PreviousScore"
]
X = df[fea_Cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)  #Split data in 4 parts #Split in size = train_size=0.5#random_state=42 - Shuffling
model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train,Y_train)
Y_Pred = model.predict(X_test)
accuracy = accuracy_score(Y_Pred,Y_test)

print(f"Higher Study hours increased the chance of passing by: {accuracy*100}%")

######################################################################
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
accuracy = accuracy_score(Y_Pred,Y_test)

print(f"Higher Attendence improves the final result by : {accuracy*100}%")


#######################################################################
#Question 6
#######################################################################

plt.figure(figsize=(7,5))
plt.hist(df["StudyHours"], bins = 5)
plt.title("Distribution of Study hours.")
plt.xlabel("Hours Studied")
plt.ylabel("Number of Students")

plt.show()

#######################################################################
#Question 7
#######################################################################

plt.figure(figsize=(7,5))

for sp in df["PreviousScore"].unique():
    temp = df[df["PreviousScore"] == sp]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label=sp)

plt.title("Scatter plot of Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()


#######################################################################
#Question 8
#######################################################################


plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")
plt.show()

#######################################################################
#Question 9
#######################################################################
plt.figure(figsize=(7,5))

for sp in df["AssignmentsCompleted"].unique():
    temp = df[df["AssignmentsCompleted"] == sp]
    plt.scatter(temp["FinalResult"], temp["AssignmentsCompleted"], label=sp)

plt.title("Plot of Assignment Completed and Final Result")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.show()


#######################################################################
#Question 10
#######################################################################
plt.figure(figsize=(7,5))

for sp in df["SleepHours"].unique():
    temp = df[df["SleepHours"] == sp]
    plt.scatter(temp["FinalResult"], temp["SleepHours"], label=sp)

plt.title("Plot of SleepHours and Final Result")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.show()





