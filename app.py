import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
from sklearn import datasets
import nltk

st.title('Test Streamlit App')

st.write('This is a test app to verify installation of all dependencies.')

# Example data and plot
df = pd.DataFrame(np.random.randn(100, 2), columns=['x', 'y'])
fig, ax = plt.subplots()
sns.scatterplot(x='x', y='y', data=df, ax=ax)
st.pyplot(fig)

st.write('Installation successful!')
