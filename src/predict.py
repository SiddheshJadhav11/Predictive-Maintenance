



import joblib



# Load trained model

model = joblib.load("models/model.pkl")



# New machine sensor values

# Format: [Temperature, Vibration, Pressure]

new_machine = [[92, 0.58, 39]]



# Predict

prediction = model.predict(new_machine)



print("=" * 50)

print("Machine Health Prediction")

print("=" * 50)



if prediction[0] == 1:

    print("⚠️ Maintenance Required")

    print("Potential equipment failure detected.")

else:

    print("✅ Machine is Healthy")

    print("No maintenance required.")
