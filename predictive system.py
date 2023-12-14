# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the trained model from the file

with open('C:/Users/Allan/Downloads/dsc-project-phase-4/model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Generate date range for future predictions

date_range = pd.date_range(start='2023-11-01', end='2028-12-31', freq='M')
# Make predictions using the loaded model
future_preds = loaded_model.predict(n_periods=len(date_range))
future_preds = np.exp(future_preds) * 100  # Rescaling

# Create a DataFrame with predictions and the corresponding dates
predictions_df = pd.DataFrame(future_preds, columns=['Energy_Predictions'], index=date_range)

# Return the predictions DataFrame
print( predictions_df)

    
