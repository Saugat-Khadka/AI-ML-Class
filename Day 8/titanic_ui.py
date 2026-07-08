import streamlit as st


st.write("# Titanic Survivor Prediction")

st.write("* If you were on titanic, would you have survived? Let's find out! *")

# Passengers Age
age = st.number_input("Enter your age", min_value=0, max_value=100)

# Passengers Gender
gender = st.selectbox("Select your gender", ("Male", "Female"))

# Passengers Class
class_options = st.selectbox("Select your class", ("1", "2", "3"))

# Passengers Sibblings/Spouses
sibs = st.number_input("Enter number of siblings/spouses aboard", min_value=0, max_value=10)

# Passengers Parents/Children
parch = st.number_input("Enter number of parents/children aboard", min_value=0, max_value=10)

# Button to predict survival
if st.button("Predict"):
    import requests

    requests.get("http://localhost:8000")


