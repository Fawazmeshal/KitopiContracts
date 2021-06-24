import pandas as pd
import streamlit as st



st.title('Hi Kitopi')

excel='C:/Users/Fawaz Almutairi/Desktop/Contractss.xlsx'
df= pd.read_excel(excel)

st.table(df)
