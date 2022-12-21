import streamlit as st
import pandas as pd
import joblib


st.title('Dog or Cat?')

height = st.number_input('Enter Height')

weight = st.number_input('Enter Weight')

eyes = st.selectbox(
	"Select Eye Colour",
	("Brown", "Blue")
)

if st.button('Submit'):
	pet_model = joblib.load('pet_model.pkl')
	
	x = pd.DataFrame([[height, weight, eyes]], columns = ['Height', 'Weight', 'Eye'])
	
	x = x.replace(['Brown', 'Blue'], [1, 0])
	
	prediction = pet_model.predict(x)[0]

	st.write(f'This instance is a {prediction}')