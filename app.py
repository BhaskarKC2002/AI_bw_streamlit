import streamlit as st
import pandas as pd

st.title("Streamlit Project")

st.write("News classification")

#taking inputs from user
data = st.text_area("Enter news for classification.")
if st.button("Submit"):
    d = {"News": [data]}
    df = pd.DataFrame(d)
    st.write(df)