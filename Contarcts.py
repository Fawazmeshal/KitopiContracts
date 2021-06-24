import pandas as pd
import streamlit as st




excel('C:/Users/Fawaz Almutairi/Desktop/Contractss.xlsx')
df= pd.read_excel(excel)


st.title('Hi Kitopi')
st.write(df)
