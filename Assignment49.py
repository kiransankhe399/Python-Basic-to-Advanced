
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance
from sklearn.metrics import classification_report

#1. Mean of a Dataset
DataSet = [6,7,8,9,10,11,12]

mean_ds = np.mean(DataSet)
print("Mean of Dataset :", mean_ds)


#2. Variance and Standard Deviation

variance = np.var(DataSet)
std_dev = np.std(DataSet)

print("Variance:", variance)
print("Standard Deviation:", std_dev)

#3. Feature Scaling using StandardScaler

dataset = [[25, 20000], [30, 40000], [35, 80000]]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataset)
print("Scaled Dataset:\n", scaled_data)

#4. Euclidean Distance Before and After Scaling
# Distance before scaling
dist_before = distance.euclidean(dataset[0], dataset[1],dataset[2])
# Distance after scaling
dist_after = distance.euclidean(scaled_data[0], scaled_data[1].scaled_data[2])

print("Distance before scaling:", dist_before)
print("Distance after scaling:", dist_after)


#7 Confusion Matrix

actual = [1,1,1,0,0,0]
predicted = [1,1,0,1,0,0]

# TP (True Positive): predicted = 1 and actual = 1 → 2

# TN (True Negative): predicted = 0 and actual = 0 → 2

# FP (False Positive): predicted = 1 but actual = 0 → 1

# FN (False Negative): predicted = 0 but actual = 1 → 1


#8
actual = np.array([1,1,1,1,0,0,0,0])
predicted = np.array([1,1,0,1,0,1,0,0])

TP = np.sum((actual == 1) & (predicted == 1))
TN = np.sum((actual == 0) & (predicted == 0))
FP = np.sum((actual == 0) & (predicted == 1))
FN = np.sum((actual == 1) & (predicted == 0))

print("TP:", TP)
print("TN:", TN)
print("FP:", FP)
print("FN:", FN)


#9 


actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

report = classification_report(actual, predicted)
print(report)

