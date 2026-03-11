import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):
    st.title("Page 1: Data Graphical Visualization")
    
    # Ensure the DataFrame has columns to visualize
    if df is not None:
    # Visualization example
        st.subheader("Bar Chart of Data")
        col = st.selectbox("Choose column for chart:", [c for c in df.columns if c != 'Hour'])

        # Plot the data with Date on the X-axis and the selected column on the Y-axis
        fig, ax = plt.subplots()
        ax.bar(df['Hour'], df[col])  # Use Date for X-axis and selected column for Y-axis
        ax.set_xlabel("Hour")
        ax.set_ylabel(col)
        ax.set_title(f"{col} Over Time")
        plt.xticks(rotation=45)  # Rotate X-axis labels for readability
        st.pyplot(fig)