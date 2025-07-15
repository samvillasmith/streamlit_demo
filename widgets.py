import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Select your age:", 0)
st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your language:", options)
st.write(f"You selected {choice}")

df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10, 20, 30, 40, 50]
})

st.write("Dataframe:")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)