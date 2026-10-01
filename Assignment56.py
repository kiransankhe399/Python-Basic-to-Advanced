import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df


# ---------------------------------------------------
# EDA
# ---------------------------------------------------

def EDA(df):

    print("\nDataset Information")
    print(df.info())

    print("\nDataset Shape")
    print(df.shape)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistical Summary")
    print(df.describe())


# ---------------------------------------------------
# Dataset Split
# ---------------------------------------------------

def splitDataset(df):

    X = df.drop("Fraud", axis=1)
    Y = df["Fraud"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    print("\nData Split Successfully")
    print("Training Records :", X_train.shape[0])
    print("Testing Records  :", X_test.shape[0])

    return X_train, X_test, Y_train, Y_test


# ---------------------------------------------------
# Evaluation Function
# ---------------------------------------------------

def evaluate_model(model, X_test, Y_test):

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred)
    recall = recall_score(Y_test, Y_pred)
    f1 = f1_score(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)

    return accuracy, precision, recall, f1, cm


# ---------------------------------------------------
# Model Training
# ---------------------------------------------------

def train_models(X_train, X_test, Y_train, Y_test):

    dt = DecisionTreeClassifier(random_state=42)

    bagging = BaggingClassifier(
        estimator=DecisionTreeClassifier(),
        n_estimators=50,
        random_state=42
    )

    rf = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    ada = AdaBoostClassifier(
        n_estimators=50,
        random_state=42
    )

    voting = VotingClassifier(
        estimators=[
            ('dt', dt),
            ('rf', rf),
            ('ada', ada)
        ],
        voting='hard'
    )

    models = {
        "Decision Tree": dt,
        "Bagging": bagging,
        "Random Forest": rf,
        "AdaBoost": ada,
        "Voting": voting
    }

    results = []

    for name, model in models.items():

        model.fit(X_train, Y_train)

        accuracy, precision, recall, f1, cm = evaluate_model(
            model,
            X_test,
            Y_test
        )

        results.append([
            name,
            round(accuracy, 4),
            round(precision, 4),
            round(recall, 4),
            round(f1, 4)
        ])

        print("\n" + "=" * 50)
        print("Model :", name)

        print("Accuracy :", round(accuracy, 4))
        print("Precision:", round(precision, 4))
        print("Recall   :", round(recall, 4))
        print("F1 Score :", round(f1, 4))

        print("\nConfusion Matrix")
        print(cm)

    comparison_df = pd.DataFrame(
        results,
        columns=[
            "Algorithm",
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ]
    )

    print("\n")
    print("=" * 60)
    print("Final Comparison")
    print("=" * 60)

    print(comparison_df)

    best_model = comparison_df.loc[
        comparison_df["F1 Score"].idxmax()
    ]

    print("\nRecommended Model:")
    print(best_model)


# ---------------------------------------------------
# Main Function
# ---------------------------------------------------

def main():

    filename = "Fraudulent_Transaction_Detection.csv"

    df = LoadData(filename)

    EDA(df)

    X_train, X_test, Y_train, Y_test = splitDataset(df)

    train_models(
        X_train,
        X_test,
        Y_train,
        Y_test
    )


if __name__ == "__main__":
    main()