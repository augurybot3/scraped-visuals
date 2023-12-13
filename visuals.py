import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

with open("data.json", "r") as file:
    data = json.load(file)
df = pd.DataFrame(data)

st.title("Alcoholic Beverages Data Visualization")

# Display Data Table
st.subheader("Data Table")
st.write(df)

# Bar Chart
st.subheader("Bar Chart - Distribution of Beverages by Brand")
brand_count = df['brand'].value_counts()
st.bar_chart(brand_count)

# Pie Chart
st.subheader("Pie Chart - Distribution by Manufacturer")
manufacturer_count = df['manufacturer'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(manufacturer_count, labels=manufacturer_count.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(plt)
