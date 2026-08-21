# Step 1: Import required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
Datapath = "PlayPredictor.csv"
df = pd.read_csv(Datapath)

print("Dataset Preview:")
print(df.head())
print("\nShape of Dataset:", df.shape)
print("\nColumn Names:", list(df.columns))
print("\nMissing Values per Column:")
print(df.isnull().sum())
print("\nClass Distribution (Play Count):")
print(df["Play"].value_counts())

# Step 3: Clean and prepare data
# Convert categorical values to numeric using LabelEncoder
le = LabelEncoder()
df["Whether"] = le.fit_transform(df["Whether"])
df["Temperature"] = le.fit_transform(df["Temperature"])
df["Play"] = le.fit_transform(df["Play"])

print("\nEncoded Dataset:")
print(df.head())

# Step 4: Split data into features and target
X = df[["Whether", "Temperature"]]
Y = df["Play"]

# Split into training and testing sets (70% train, 30% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Step 5: Train model using KNN
k = 3  # number of neighbors
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, Y_train)

# Step 6: Test model
Y_pred = model.predict(X_test)
print("\nPredicted Values:", Y_pred)

# Step 7: Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)
print("\nAccuracy of KNN Classifier (k=3):", round(accuracy * 100, 2), "%")

# Step 8: Function to check accuracy for different k values
def CheckAccuracy():
    for k in range(1, 8):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        acc = accuracy_score(Y_test, Y_pred)
        print(f"k = {k} → Accuracy = {round(acc * 100, 2)}%")

print("\nAccuracy for different k values:")

def main():
    CheckAccuracy()

if __name__ == "__main__":
    main()
