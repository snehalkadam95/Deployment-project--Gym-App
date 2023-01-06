# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing dependancies
import numpy as np
import pickle
import sklearn


# loading the saved model
model = pickle.load(open('C:/Users/DELL/Desktop/Gym project/trained_model.sav', 'rb'))


# creating a function for Prediction
input_data = (58,4.10,45)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('You are Extremely obese')

elif (prediction[0] == 1):
  print('You are Healthy')

elif (prediction[0] == 2):
  print('You are Obese')

elif (prediction[0] == 3):
  print('You are Overweight') 

else:
 print('You are Under weight')