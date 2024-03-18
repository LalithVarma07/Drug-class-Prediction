import streamlit as st
import joblib
import numpy as np

saved_model = joblib.load("Drug Class Prediction.joblib")

# Define the prepare_input function to preprocess input data
def prepare_input(age, sex, bp_level, cholesterol_level, na_to_k_ratio):
    sex = 1 if sex == "Male"else 0
    if bp_level == "High":
        bp_level = 0
    elif bp_level == "Low":
        bp_level = 1
    else: 
        bp_level = 2
    cholesterol_level = 0 if cholesterol_level == "High" else 1
    # Convert categorical variables to numerical values

    input_data = np.array([[age, sex, bp_level, cholesterol_level, na_to_k_ratio]])
    return input_data

def predict_drug(age, sex, bp_level, cholesterol_level, na_to_k_ratio):
    input_data = prepare_input(age, sex, bp_level, cholesterol_level, na_to_k_ratio)
    prediction = saved_model.predict(input_data)
    return prediction

def main():
    st.title("Drug Class Prediction")

    # Collecting user inputs
    age = st.number_input("Age", min_value=0)
    sex = st.selectbox("Sex", ["Female","Male"])
    bp_level = st.selectbox("Blood Pressure Level",["High","Low","Normal"])
    cholesterol_level = st.selectbox("Cholesterol Level",["High","Normal"])
    na_to_k_ratio = st.number_input("Na to K Ratio", min_value=0.0)

    # Button to make prediction
    if st.button("Predict Drug Class"):
        # Calling the drug prediction function
        predicted_drug = predict_drug(age, sex, bp_level, cholesterol_level, na_to_k_ratio)
        if predicted_drug == 0:
            st.write("Predicted Drug class is 'Beta Blockers'")
        if predicted_drug == 1:
            st.write("Predicted Drug class is 'ACE Inhibitors'")
        if predicted_drug == 2:
            st.write("Predicted Drug class is 'Statins'")
        if predicted_drug == 3:
            st.write("Predicted Drug class is 'Diuretics'")
        if predicted_drug == 4:
            st.write("Predicted Drug class is 'Antiplatelet Agents'")


if __name__ == "__main__":
    main()
