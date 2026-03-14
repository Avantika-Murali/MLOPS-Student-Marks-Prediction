# MLOps Student Pass Prediction

This is a simple MLOps project for evaluation.

## Steps

1. Train model
```
python train.py
```

2. Run API
```
python app.py
```

3. Build Docker
```
docker build -t mlops-project .
```

4. Run Docker
```
docker run -p 5000:5000 mlops-project
```

5. Deploy using Railway connected to GitHub repository.

API endpoint:
POST /predict

Example JSON:
{
 "hours": 6
}