import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# ==============================
# Step 1 : Load Dataset
# ==============================
def LoadData(filename):

    df = pd.read_csv(filename)

    print("\nDataset Loaded Successfully")
    print(df.head())

    return df


# ==============================
# Step 2 : EDA
# ==============================
def EDA(df):

    print("\n----- Dataset Information -----")
    print(df.info())

    print("\n----- Dataset Shape -----")
    print(df.shape)

    print("\n----- Missing Values -----")
    print(df.isnull().sum())

    print("\n----- Statistical Summary -----")
    print(df.describe())


# ==============================
# Step 3 : Split Dataset
# ==============================
def SplitData(df):

    X = df.drop("LoanApproved", axis=1)
    Y = df["LoanApproved"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42
    )

    print("\nData Split Successfully")
    print("Training Records :", X_train.shape[0])
    print("Testing Records  :", X_test.shape[0])

    return X_train, X_test, Y_train, Y_test


# ==============================
# Step 4 : Feature Scaling
# ==============================
def ScaleData(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\nFeature Scaling Completed")

    return X_train_scaled, X_test_scaled


# ==============================
# Step 5 : Logistic Regression
# ==============================
def LogisticModel(X_train, X_test, Y_train, Y_test):

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(
        f"Accuracy using Logistic Regression : {accuracy*100:.2f}%")

    return model, accuracy


# ==============================
# Step 6 : Decision Tree
# ==============================
def DecisionTreeModel(X_train, X_test, Y_train, Y_test):

    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(
        f"Accuracy using Decision Tree : {accuracy*100:.2f}%")

    return model, accuracy


# ==============================
# Step 7 : KNN
# ==============================
def KNNModel(X_train, X_test, Y_train, Y_test):

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(
        f"Accuracy using KNN : {accuracy*100:.2f}%")

    return model, accuracy


# ==============================
# Step 8 : Hard Voting
# ==============================
def HardVotingClassifierModel(
        X_train,
        X_test,
        Y_train,
        Y_test):

    lr_model = LogisticRegression(
        max_iter=1000,
        random_state=42)

    dt_model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42)

    knn_model = KNeighborsClassifier(
        n_neighbors=5)

    voting_model = VotingClassifier(
        estimators=[
            ('lr', lr_model),
            ('dt', dt_model),
            ('knn', knn_model)
        ],
        voting='hard'
    )

    voting_model.fit(X_train, Y_train)

    Y_pred = voting_model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(
        f"Accuracy using Hard Voting : {accuracy*100:.2f}%")

    return voting_model, accuracy


# ==============================
# Step 9 : Soft Voting
# ==============================
def SoftVotingClassifierModel(
        X_train,
        X_test,
        Y_train,
        Y_test):

    lr_model = LogisticRegression(
        max_iter=1000,
        random_state=42)

    dt_model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42)

    knn_model = KNeighborsClassifier(
        n_neighbors=5)

    voting_model = VotingClassifier(
        estimators=[
            ('lr', lr_model),
            ('dt', dt_model),
            ('knn', knn_model)
        ],
        voting='soft'
    )

    voting_model.fit(X_train, Y_train)

    Y_pred = voting_model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(
        f"Accuracy using Soft Voting : {accuracy*100:.2f}%")

    return voting_model, accuracy



def main():

    # Load Dataset
    df = LoadData("Customer_Loan_Approval.csv")

    # EDA
    EDA(df)

    # Split Data
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Scaling
    X_train_scaled, X_test_scaled = ScaleData(
        X_train,
        X_test
    )

    print("\n========== MODEL TRAINING ==========\n")

    # Logistic Regression
    lr_model, lr_acc = LogisticModel(
        X_train_scaled,
        X_test_scaled,
        Y_train,
        Y_test
    )

    # Decision Tree
    dt_model, dt_acc = DecisionTreeModel(
        X_train,
        X_test,
        Y_train,
        Y_test
    )

    # KNN
    knn_model, knn_acc = KNNModel(
        X_train_scaled,
        X_test_scaled,
        Y_train,
        Y_test
    )

    # Hard Voting
    hard_model, hard_acc = HardVotingClassifierModel(
        X_train_scaled,
        X_test_scaled,
        Y_train,
        Y_test
    )

    # Soft Voting
    soft_model, soft_acc = SoftVotingClassifierModel(
        X_train_scaled,
        X_test_scaled,
        Y_train,
        Y_test
    )

    # Comparison
    print("\n========== MODEL COMPARISON ==========\n")

    results = {
        "Logistic Regression": lr_acc,
        "Decision Tree": dt_acc,
        "KNN": knn_acc,
        "Hard Voting": hard_acc,
        "Soft Voting": soft_acc
    }

    for model, acc in results.items():
        print(f"{model:<25} : {acc*100:.2f}%")

    # Save Best Model
    joblib.dump(soft_model, "LoanApprovalModel.pkl")

    print("\nBest Model Saved Successfully")
    print("File Name : LoanApprovalModel.pkl")



if __name__ == "__main__":
    main()