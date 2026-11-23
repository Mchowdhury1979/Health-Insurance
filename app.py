
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Healthcare Insurance Dashboard",
    layout="wide"
)

st.title("Healthcare Insurance Charges Dashboard")

# Load cleaned data
#df = pd.read_csv("insurance_cleaned.csv")
DATA_PATH = r"C:\Users\Mchow\Documents\health-insurance\insurance_cleaned.csv"

df = pd.read_csv(DATA_PATH)

# Sidebar filters
st.sidebar.header("Filters")

smoker_options = ["All"] + sorted(df["smoker"].unique().tolist())

selected_smoker = st.sidebar.selectbox(
    "Smoking status",
    smoker_options
)

region_options = ["All"] + sorted(df["region"].unique().tolist())

selected_region = st.sidebar.selectbox(
    "Region",
    region_options
)

# Filter data
filtered_df = df.copy()

if selected_smoker != "All":
    filtered_df = filtered_df[
        filtered_df["smoker"] == selected_smoker
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["region"] == selected_region
    ]

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Number of records",
    len(filtered_df)
)

col2.metric(
    "Mean charges",
    f"${filtered_df['charges'].mean():,.2f}"
)

col3.metric(
    "Median charges",
    f"${filtered_df['charges'].median():,.2f}"
)

# Smoking status chart
st.subheader("Insurance Charges by Smoking Status")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=filtered_df,
    x="smoker",
    y="charges",
    ax=ax
)

ax.set_xlabel("Smoking Status")
ax.set_ylabel("Insurance Charges")
ax.set_title("Charges by Smoking Status")

st.pyplot(fig)

# Region chart
st.subheader("Mean Charges by Region")

region_summary = (
    filtered_df.groupby("region")["charges"]
    .mean()
    .reset_index()
)

fig2, ax2 = plt.subplots(figsize=(8, 5))

sns.barplot(
    data=region_summary,
    x="region",
    y="charges",
    ax=ax2
)

ax2.set_xlabel("Region")
ax2.set_ylabel("Mean Charges")
ax2.set_title("Average Charges by Region")

st.pyplot(fig2)

# Age relationship
st.subheader("Age vs Insurance Charges")

fig3, ax3 = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=filtered_df,
    x="age",
    y="charges",
    hue="smoker",
    ax=ax3
)

ax3.set_xlabel("Age")
ax3.set_ylabel("Insurance Charges")

st.pyplot(fig3)

# BMI relationship
st.subheader("BMI vs Insurance Charges")

fig4, ax4 = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=filtered_df,
    x="bmi",
    y="charges",
    hue="smoker",
    ax=ax4
)

ax4.set_xlabel("BMI")
ax4.set_ylabel("Insurance Charges")

st.pyplot(fig4)

# View filtered data
st.subheader("Filtered Dataset")

st.dataframe(filtered_df)
