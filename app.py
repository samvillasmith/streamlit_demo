import streamlit as st 
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello World!")

# Display text in the app
st.write("This is an example text for the web app")

# Display a simple dataframe
df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10, 20, 30, 40, 50]
})

st.write("Dataframe:")
st.write(df)

# Sample data visualization - line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a','b','c']
)
st.line_chart(chart_data)