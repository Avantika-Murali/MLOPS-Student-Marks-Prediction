from flask import Flask, render_template, request
import os
import pickle

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])  # get hours input

    prediction = model.predict([[hours]])
    marks = prediction[0]

    # pass fail logic
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return render_template(
        "index.html",
        prediction_text=f"Predicted Marks: {round(marks,2)} - Result: {result}"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)