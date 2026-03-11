import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):
    st.title("Page 2: Data Graphical Visualization")
    
    # Ensure the DataFrame has columns to visualize
    if df is not None:
    # Line Plot
        st.subheader("Line Plot of Selected Data Over Time")
        date_column = st.selectbox("Choose a date/time column for line plot:", df.columns)
        col_line = st.selectbox("Choose column for the line chart:", [c for c in df.columns if c != 'Hour'])
        if date_column and col_line:
            fig, ax = plt.subplots()
            ax.plot(df[date_column], df[col_line], color='blue', marker='o', linestyle='-')
            ax.set_xlabel(date_column)
            ax.set_ylabel(col_line)
            ax.set_title(f"{col_line} Over Time")
            plt.xticks(rotation=45)
            st.pyplot(fig)
