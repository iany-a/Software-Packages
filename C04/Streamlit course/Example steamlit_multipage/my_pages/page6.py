import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app(df):
    st.title("Page 6: Data Graphical Visualization")
    
    # Ensure the DataFrame has columns to visualize
    if df is not None:
       
        # Histogram
        st.subheader("Distribution of Selected Column")
        column_hist = st.selectbox("Choose column for histogram:", df.columns)
        if column_hist:
            fig, ax = plt.subplots()
            ax.hist(df[column_hist], bins=20, color='purple', edgecolor='black')
            ax.set_xlabel(column_hist)
            ax.set_ylabel("Frequency")
            ax.set_title(f"Distribution of {column_hist}")
            st.pyplot(fig)

        # Box Plot
        st.subheader("Box Plot for Outlier Detection")
        column_box = st.selectbox("Choose column for box plot:", df.columns)
        if column_box:
            fig, ax = plt.subplots()
            ax.boxplot(df[column_box].dropna(), vert=False)
            ax.set_xlabel(column_box)
            ax.set_title(f"Box Plot of {column_box}")
            st.pyplot(fig)