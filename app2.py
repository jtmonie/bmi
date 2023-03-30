import streamlit as st
from PIL import Image

st.title("BMI Calculator App")

w=st.number_input("what is your weight in KG")
h=st.number_input("what is your height in metres")

def bmi_index(w,h):
    bmi = round(w / (h**2),2)
    if bmi >= 30:
        return f'Your Bmi score is {bmi} and you are at risk of being extremely obese'
    elif bmi >= 25:
        return f'Your Bmi score is {bmi} and you are at risk of being overweight'
    elif bmi >= 18.5:
        return f'Your Bmi score is {bmi} and you are very healthy'
    else:
        return f'Your Bmi score is {bmi} and you are at risk of being underweight'
    
if st.button("Calculate BMI"):
    st.write(bmi_index(w,h))