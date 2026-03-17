from preprocess import load_data, preprocess_data
from train import train_model, save_model
from evaluate import evaluate_model

# Load
df = load_data("C:/Users/aswin/OneDrive/Desktop/github/student-placement-prediction-ml/dataset/Placement_Data_Full_Class.csv")

# Preprocess
df = preprocess_data(df)

# Train
model, X_test, y_test = train_model(df)

# Evaluate
evaluate_model(model, X_test, y_test)

# Save
save_model(model)