# app.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# 🔁 Load model and features
model = joblib.load('trained_data/student_pass_fail_model.pkl')
features = joblib.load('trained_data/student_features.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # 🧾 Create DataFrame
    input_df = pd.DataFrame([data])
    input_df = input_df.reindex(columns=features, fill_value=0)  # Ensure correct format

    # 🔮 Predict
    result = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return jsonify({
        "Result": "Passed" if result == 1 else "Failed",
        "Probability_Passed": round(probability, 3)
    })

if __name__ == '__main__':
    app.run(debug=True)
