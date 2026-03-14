from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return "ML Model Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    hours = data["hours"]

    prediction = model.predict([[hours]])

    result = "Pass" if prediction[0]==1 else "Fail"

    return jsonify({"prediction":result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)