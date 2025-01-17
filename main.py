import os
import numpy as np
import cv2
import joblib
import pandas as pd
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title('Charge&Guess')
st.markdown('''
Please use input data
''')


st.sidebar.title("Operations on the Dataset")

#st.subheader("Checkbox")
w1 = st.sidebar.checkbox("Sample data ", False)

#have to load model in ('')
#reg_model = joblib.load('CV_RF_Regression.h5')#Run to ok
model_file = joblib.load('CV_RF_Regression.h5')



if w1:
    st.write('Sample data')
    image = Image.open('data_charges.png')
    st.image(image, 'Sample data')
'''
col1, col2, col3 , col4, col5, col6= st.columns(6)
    
with col1:
    st.header("Age")
    age = st.number_input('Insert age')
    st.write('The current number is ', age)
    
with col2:
    st.header("Sex")
    sex = st.selectbox(
     'gender',
     ('male', 'female'))

    st.write('You selected:', sex)
    
with col3:
    st.header("BMI")
    bmi = st.number_input('Insert bmi')
    st.write('The current number is ', bmi)
    
with col4:
    st.header("Child")
    children = st.number_input('Insert no of children')
    st.write('The current number is ', children)
    
with col5:
    st.header("smoker")
    smoker = st.selectbox(
     'smoker',
     ('yes', 'no'))

    st.write('You selected:', smoker)
    
    
with col6:
    st.header("region")
    region = st.selectbox(
     'Region',
     ('southeast', 'southwest','northeast','northwest'))

    st.write('You selected:', region)
    
'''

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Age")
    age = st.number_input('Insert age')
    st.write('The current number is ', age)
    
with col2:
    st.header("Sex")
    sex = st.selectbox(
     'gender',
     ('male', 'female'))

    st.write('You selected:', sex)
    if sex == 'male':
        sex = 1
    else:
        sex = 0
    st.write('You selected:', sex)
    
with col3:
    st.header("BMI")
    bmi = st.number_input('Insert bmi')
    st.write('The current number is ', bmi)


col4, col5, col6 = st.columns(3)
with col4:
    st.header("Child")
    children = st.number_input('Insert no of children')
    st.write('The current number is ', children)
    
with col5:
    st.header("smoker")
    smoker = st.selectbox(
     'smoker',
     ('yes', 'no'))

    st.write('You selected:', smoker)
    if smoker == 'yes':
        smoker = 1
    else:
        smoker = 0
    st.write('You selected:', smoker)
    
    
with col6:
    st.header("region")
    region = st.selectbox(
     'Region',
     ('southeast', 'southwest','northeast','northwest'))
    
    st.write('You selected:', region)
    if region == 'northeast':
        region = 0
    if region == 'northwest':
        region = 1
    if region == 'southeast':
        region = 2
    else:
        region = 3
    st.write('You selected:', region)
    
data_pre = ([[age,sex,bmi,children,smoker,region]])



ok = st.button("Calculate charges")

if ok:
    #st.write([age,sex,bmi,children,smoker,region])
    st.write(data_pre)
    #charges = reg_model.predict(data_pre)
    charges = model_file.predict(data_pre)
    st.write(charges)

    #st.subheader(f"The estimated charges is ${charges['Label'][0]:.2f}")
