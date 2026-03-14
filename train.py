import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import mlflow
import mlflow.sklearn

data = {
    "hours":[1,2,3,4,5,6,7,8],
    "pass":[0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["pass"]

model = LogisticRegression()

mlflow.start_run()

model.fit(X,y)

mlflow.log_param("model","LogisticRegression")

mlflow.sklearn.log_model(model,"model")

pickle.dump(model, open("model.pkl","wb"))

mlflow.end_run()

print("Model trained successfully")