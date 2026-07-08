# UI for titanic prediction

import streamlit as st
import requests as req

st.title("Titanic Survival Prediction")
st.write("This app predicts whether a passenger survived the Titanic disaster based on their features.")
st.write("Note: This is a demo app and the predictions are based on a pre-trained model. The results may not be accurate.")
st.write("Let's see if you would have survived the Titanic disaster!")

#form
st.write("## Passenger Details")

# Passenger's Age
age = st.number_input("Age", min_value=0, max_value=100, value=30)

#Passenger's Gender
gender = st.selectbox("Gender", options=["male", "female"]) 

# Passenger's Class
pclass = st.selectbox("Passenger Class", options=[1, 2, 3])

# Number of Siblings/Spouses Aboard
sibsp = st.number_input("Number of Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)

# Number of Parents/Children Aboard
parch = st.number_input("Number of Parents/Children Aboard", min_value=0, max_value=10, value=0)  


if st.button("Predict"):
    # Load the model
    url = "http://localhost:8000/predict"
    
    payload = {
        "age": age,
        "gender": gender,
        "pclass": pclass,
        "sibsp": sibsp,
        "parch": parch
    }
    try:
        # API expects query parameters, send as params
        response = req.post(url, params=payload)
        if response.status_code == 200:
            result = response.json()
            if "prediction" in result:
                prediction = result["prediction"]
                if prediction == 1:
                    st.success("The Demo Model has predicted that you would have survived the Titanic disaster!")
                else:
                    st.warning("The Demo Model has predicted that you would not have survived the Titanic disaster.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {str(e)}")