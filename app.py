import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Slider for year range
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))

# Filter data
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample
st.write("Sample Data:", filtered_df.head())

# Plot
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)
