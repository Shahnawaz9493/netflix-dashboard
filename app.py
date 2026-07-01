import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Netflix Data Analysis", layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    return df

df = load_data()

# ---------------- LOAD CSS ----------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- TITLE ----------------
st.title("🎬 Netflix Data Analysis Dashboard")

# ---------------- BASIC CLEANING ----------------
df = df.dropna(subset=["type", "country", "release_year", "listed_in"])

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

content_type = st.sidebar.multiselect(
    "Select Type",
    df["type"].unique(),
    default=df["type"].unique()
)

year_range = st.sidebar.slider(
    "Release Year Range",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (2015, 2021)
)

filtered_df = df[
    (df["type"].isin(content_type)) &
    (df["release_year"].between(year_range[0], year_range[1]))
]

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(filtered_df))
col2.metric("Movies", len(filtered_df[filtered_df["type"] == "Movie"]))
col3.metric("TV Shows", len(filtered_df[filtered_df["type"] == "TV Show"]))

# ---------------- CHART 1: TYPE DISTRIBUTION ----------------
st.subheader("Content Type Distribution")

type_count = filtered_df["type"].value_counts().reset_index()
type_count.columns = ["Type", "Count"]

fig1 = px.bar(type_count, x="Type", y="Count", color="Type")
st.plotly_chart(fig1, use_container_width=True)

# ---------------- CHART 2: TOP COUNTRIES ----------------
st.subheader("Top Countries Producing Content")

country_count = (
    filtered_df["country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country_count.columns = ["Country", "Count"]

fig2 = px.bar(country_count, x="Country", y="Count")
st.plotly_chart(fig2, use_container_width=True)

# ---------------- CHART 3: RELEASE TREND ----------------
st.subheader("Content Release Trend")

year_count = (
    filtered_df["release_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_count.columns = ["Year", "Count"]

fig3 = px.line(year_count, x="Year", y="Count", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# ---------------- RAW DATA ----------------
st.subheader("Raw Data")
st.dataframe(filtered_df)