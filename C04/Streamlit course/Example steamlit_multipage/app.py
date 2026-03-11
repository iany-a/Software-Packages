import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_pages import page1, page2, page3, page4, page5, page6  # Import the page modules

# Create a dictionary to store page names and functions
PAGES = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    "Page 6": page6
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Title and header
st.title("My Streamlit App")
st.header("Data Analysis and Visualization")

# Adding a widget
st.subheader("Upload a CSV File")
file = st.file_uploader("Choose a file", type="csv")

# Load and display data
if file:
    df = pd.read_csv(file)
    # Call the app function for the selected page and pass the DataFrame
    PAGES[selection].app(df)         
else:
    st.write("Please upload a CSV file to proceed.")