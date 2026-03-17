from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(df):
    X = df.drop("status", axis=1)
    y = df["status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    return model, X_test, y_test

def save_model(model):
    pickle.dump(model, open("C:/Users/aswin/OneDrive/Desktop/github/student-placement-prediction-ml/model/model.pkl", "wb"))