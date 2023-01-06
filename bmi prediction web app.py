# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:55:15 2023

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st
import sklearn

# loading the saved model
model = pickle.load(open('C:/Users/DELL/Desktop/Gym project/trained_model.sav', 'rb'))

#creating a function for prediction

def bmi_prediction(input_data):
   

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'You are Extremely obese'

    elif (prediction[0] == 1):
      return 'You are Healthy'

    elif (prediction[0] == 2):
      return'You are Obese'

    elif (prediction[0] == 3):
      return'You are Overweight'

    else:
      return 'You are Under weight'
  
    
def main():
    
    #Giving title
    st.title("BMI Prediction Web App")
    
    #Getting empty data from user
    
    Age = st.text_input("AGE")
    Height = st.text_input("HEIGHT")
    weight = st.text_input("WEIGHT")
  
    #Code for prediction
    checking=''
    
    #creating button for prediction
    if st.button("BMI Prediction Result"):
        checking= bmi_prediction([Age,Height,weight])
        
        st.success(checking)
        
if __name__ == '__main__':
    main()
    