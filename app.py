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
    hours = float(request.form['hours'])

    prediction = model.predict([[hours]])
    marks = float(prediction[0])

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return render_template(
        "index.html",
        prediction_text=f"Study Hours: {hours} | Predicted Marks: {round(marks,2)} | Result: {result}"
    )