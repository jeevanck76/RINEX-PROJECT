%%writefile app.py
#%%writefile app.py is a magic command which creates a file named app.py
import streamlit as st
import joblib
import numpy as np
model = joblib .load('weather prediction')
st.title('WEATHER PREDICTION')
st.write("this is a app to predict the weather condition in a certain region by getting details of the xweather")
ip1 = st.number_input('Enter the precipitation')
ip2 = st.number_input('Enter the temp_max')
ip3 = st.number_input('Enter the temp_min')
ip4 = st.number_input('Enter the wind')
ls1=np.append(ip1,ip2)
ls2=np.append(ip3,ip4)
ls=np.append(ls1,ls2)
op = model.predict([ls])
if st.button('Predict'):
  st.title(op[0]) 
