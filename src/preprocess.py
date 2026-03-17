import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    # Drop unnecessary column
    df = df.drop("salary", axis=1)

    # Convert target
    df["status"] = df["status"].map({"Placed": 1, "Not Placed": 0})

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df