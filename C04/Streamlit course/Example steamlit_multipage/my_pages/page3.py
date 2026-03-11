import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app(df):
    st.title("Page 3: Data Graphical Visualization")
    
    # Ensure the DataFrame has columns to visualize
    if df is not None:
        # Scatter Plot
        st.subheader("Scatter Plot for Comparative Analysis")
        x_axis = st.selectbox("Choose X-axis column:", df.columns)
        y_axis = st.selectbox("Choose Y-axis column:", [c for c in df.columns if c != x_axis])
        if x_axis and y_axis:
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis], color='green', alpha=0.5)
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f"{y_axis} vs {x_axis}")
            st.pyplot(fig)