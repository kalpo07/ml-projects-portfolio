from flask import Flask, request, jsonify
import joblib, pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=features, fill_value=0)

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    return jsonify({"prediction": int(pred), "probability": float(prob)})

if __name__ == "__main__":
    app.run(debug=True)
