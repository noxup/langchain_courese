import  streamlit as st
import pandas as pd
import numpy as np

st.title("My first Streamlit app")

## display text
st.write("this is the simple text")

## create data frame 

df = pd.DataFrame({
    "first column": [1,2,3,4],
    "second column": [10,20,30,40]
})


## display data frame
st.write("here is the dataframe")
st.write(df)

## draw line chart 

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.line_chart(chart_data)