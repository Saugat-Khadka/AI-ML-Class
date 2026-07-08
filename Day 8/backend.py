from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Titanic Survival Prediction API!"}

@app.post("/predict")
def predict(age: int, gender: str, pclass: int, sibsp: int, parch: int):
    # return {"message": "Prediction endpoint is working!"}
    import joblib
    import pandas as pd
    # # Load the model
    try:
            model = joblib.load("titanic_model.pkl")
    except Exception as e:
        return {"error": f"Failed to load model: {str(e)}"}

    # # Prepare the input data
    data = pd.DataFrame({
        "Age": [age],
        "Pclass": [pclass],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Gender": [1 if gender == "male" else 0]
    })

    #input_data = pd.DataFrame([[age, pclass, sibsp, parch, 1 if gender == "male" else 0]], columns=["Age", "Pclass", "SibSp", "Parch", "Gender"])     

    # # Make prediction
    prediction = model.predict(data)  

    return {"prediction": int(prediction[0])}