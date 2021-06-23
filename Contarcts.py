import streamlit as st
import pandas as pd


st.title('Hello, my name is fawaz and i creat a dashboard')


excel= 'C:\Users\Fawaz Almutairi\Desktop\Contractss.xlsx'
df=pd.read_excel(excel, usecols='A:D', sheet_name=0, index_col=0)
st.table(df)
