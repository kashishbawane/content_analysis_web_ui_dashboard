# app.py
import streamlit as st
from data_cleaning import load_data
import plotly.express as px

st.set_page_config(page_title="🎬 Content Analysis Dashboard", layout="wide")

st.title("🎬 Content Analysis Dashboard")

# Load dataset
df = load_data()
st.write("✅ Data Loaded. Columns:", list(df.columns))

# Example charts
if "Genre" in df.columns:
    st.subheader("📊 Genre Distribution")
    fig = px.bar(df["Genre"].value_counts().reset_index(),
                 x="index", y="Genre", labels={"index": "Genre", "Genre": "Count"})
    st.plotly_chart(fig, use_container_width=True)

if "Certificate" in df.columns:
    st.subheader("🎫 Certificate Distribution")
    fig = px.pie(df, names="Certificate", title="Certificates Share")
    st.plotly_chart(fig, use_container_width=True)

if "Director" in df.columns:
    st.subheader("🎥 Top Directors")
    fig = px.bar(df["Director"].value_counts().nlargest(10).reset_index(),
                 x="index", y="Director", labels={"index": "Director", "Director": "Count"})
    st.plotly_chart(fig, use_container_width=True)

# Show raw data
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())
