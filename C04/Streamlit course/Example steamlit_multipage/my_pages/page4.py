import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app(df):
    st.title("Page 4: Data Tabular & Graphical Visualization")
    # Summary Statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())
    
    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    #fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(12, 8))  # Enlarged heatmap
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

    # Data Download Option
    st.subheader("Download Processed Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )