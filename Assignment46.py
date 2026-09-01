import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 1: Load Data
df = pd.read_csv("Advertising.csv")
print(df.head())

# Step 2: Clean and Prepare Data
if "Unnamed: 0" in df.columns:
    df = df.drop(columns="Unnamed: 0")

print(df.isnull().sum())
print(df.corr())

# Step 3: Define Features and Target
X = df[["TV", "Radio", "Newspaper"]]  
Y = df["Sales"]

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# Step 4: Train Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Step 5: Test Model
Y_pred = model.predict(X_test)

print("Predicted Sales:", Y_pred)

# Step 6: Evaluate Model
r2 = r2_score(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)

print(f"R² Score: {r2:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
