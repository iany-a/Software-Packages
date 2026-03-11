import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app(df):
    st.title("Page 5: Data Tabular Visualization")
    st.write("Data Preview:", df.head()) 