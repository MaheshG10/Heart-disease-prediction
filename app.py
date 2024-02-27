import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('heart_disease_model.pkl', 'rb'))


# Define the function to predict heart disease
def Predict_Heart_Disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    sex = 1 if sex == 'Male' else 0
    fbs = 1 if fbs == 'True' else 0
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    return prediction


# Defining the Streamlit application
def App():
    st.title('Heart Disease Prediction')
    st.write('Input the following parameters to predict the risk of heart disease:')
    age = st.number_input('Age:', min_value=10, max_value=100, value=25)
    # age = st.slider('Age', 20, 100, 50)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.number_input('Chest Pain Type', min_value=0,max_value=3,value=0)
    trestbps = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
    chol = st.slider('Cholesterol (mg/dL)', 100, 600, 200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['False', 'True'])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.number_input('Maximum Heart Rate Achieved', 70, 220, 150)
    exang = st.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.0, 3.0, 0.1)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.number_input('Number of Major Vessels Colored by Flourosopy', min_value=0,max_value=3,value=0)
    thal = st.number_input('Thalassemia', min_value=0,max_value=3,value=0)

    # Prediction of the risk assessment
    if st.button('Predict'):
        result = Predict_Heart_Disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,thal)
        if result == 0:
            st.write('No Heart Disease Detected for the Candidate ')
        else:
            st.write('The Candidate has risk of Heart Disease!! Consult Doctor Immediately ')


if __name__ == '__main__':
    App()