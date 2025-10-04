import streamlit as st
from data_cleaning import load_data
import plotly.express as px

st.set_page_config(page_title="🎬 Content Analysis Dashboard", layout="wide")

st.title("🎬 Content Analysis Dashboard")

df = load_data()
st.write("✅ Data Loaded. Columns:", list(df.columns))

# Genre Analysis
if "Genre" in df.columns:
    st.subheader("📊 Genre Distribution")
    genre_counts = df["Genre"].value_counts().reset_index()
    genre_counts.columns = ["Genre", "Count"]
    fig = px.bar(genre_counts, x="Genre", y="Count", title="Content Count by Genre")
    st.plotly_chart(fig, use_container_width=True)

# Certificate Analysis
if "Certificate" in df.columns:
    st.subheader("🎫 Certificate Distribution")
    cert_counts = df["Certificate"].value_counts().reset_index()
    cert_counts.columns = ["Certificate", "Count"]
    fig = px.pie(cert_counts, names="Certificate", values="Count", title="Certificates Share")
    st.plotly_chart(fig, use_container_width=True)

# Director Analysis
if "Director" in df.columns:
    st.subheader("🎥 Top Directors")
    director_counts = df["Director"].value_counts().nlargest(10).reset_index()
    director_counts.columns = ["Director", "Count"]
    fig = px.bar(director_counts, x="Director", y="Count", title="Top 10 Directors")
    st.plotly_chart(fig, use_container_width=True)

# Data Preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())
