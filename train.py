import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import mlflow
import mlflow.sklearn

# Example data for study hours and corresponding marks
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [20, 30, 40, 50, 60, 70, 80, 90]  # numeric marks, continuous
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["marks"]

model = LinearRegression()

mlflow.start_run()

model.fit(X, y)

mlflow.log_param("model", "LinearRegression")

mlflow.sklearn.log_model(model, "model")

pickle.dump(model, open("model.pkl", "wb"))

mlflow.end_run()

print("Model trained successfully")