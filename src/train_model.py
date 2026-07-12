



import os

import joblib

import pandas as pd



from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report





# Load dataset

df = pd.read_csv("data/machine_data.csv")



# Select features and target

X = df[["Temperature", "Vibration", "Pressure"]]

y = df["Failure"]



# Split dataset

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)



# Create model

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)



# Train model

model.fit(X_train, y_train)



# Make predictions

predictions = model.predict(X_test)



# Evaluate model

accuracy = accuracy_score(y_test, predictions)



print("=" * 50)

print("Predictive Maintenance Model")

print("=" * 50)

print(f"Model Accuracy : {accuracy:.2f}")

print("\nClassification Report\n")

print(classification_report(y_test, predictions))



# Save trained model

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/model.pkl")



print("\nModel saved successfully.")

print("Location : models/model.pkl")
