# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:36:58 2023

@author: Allan
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st


# Load the trained model from the file

with open('C:/Users/Allan/Downloads/dsc-project-phase-4/model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
# creating a function for prediction

def Energy_Prediction(date_range):
    

    date_range = pd.date_range(start='2023-11-01', end='2026-12-01', freq='M')
    # Make predictions using the loaded model
    future_preds = loaded_model.predict(n_periods=len(date_range))
    future_preds = np.exp(future_preds) * 100  # Rescaling

    # Create a DataFrame with predictions and the corresponding dates
    predictions_df = pd.DataFrame(future_preds, columns=['Energy_Predictions'], index=date_range)

    # Return the predictions DataFrame
   
    return predictions_df    



def main():
    
    #Giving a title
    st.title('Energy Production Web App')
    
    #Getting the input data from the user
    
    # Get date input from user
    Date = st.date_input("Date")

    # Get energy production input from user
    #Energy_production = st.number_input("Energy Production")
    
    
    #Code for prediction
    Energy_production = ''
    
    #creating a partern for prediction
    
    if st.button('Energy Prediction'):
        Energy_production = Energy_Prediction([Date])
        
    st.success(Energy_production)
    
    
    
if __name__ == '__main__':
    main()
    