# app.py

import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Simple Streamlit App for EB Deployment Test")

    st.write("Hello! This is a simple Streamlit app to test EB deployment.")

    st.header("Random Data Visualization")
    
    # Generate some random data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C'])

    # Display the data as a chart
    st.line_chart(chart_data)

    st.header("Interactive Widget")
    
    # Add a slider
    x = st.slider('Select a value')
    st.write(f"You selected: {x}")

    st.header("Deployment Info")
    st.write("If you can see this, your Streamlit app is successfully deployed on Elastic Beanstalk!")

if __name__ == "__main__":
    main()
