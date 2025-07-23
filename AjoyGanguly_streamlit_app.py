
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("sales_data.csv")

df = load_data()

st.title("InsightForge: AI-Powered Business Intelligence Assistant")

st.sidebar.header("Filter Parameters")
selected_store = st.sidebar.selectbox("Select Store", df["Store"].unique())
selected_item = st.sidebar.selectbox("Select Item", df["Item"].unique())

filtered_data = df[(df["Store"] == selected_store) & (df["Item"] == selected_item)]

st.subheader("Filtered Sales Data")
st.write(filtered_data)

st.subheader("Sales Trend")
fig, ax = plt.subplots()
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])
filtered_data = filtered_data.sort_values("Date")
ax.plot(filtered_data["Date"], filtered_data["Sales"], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

st.markdown("Use natural language to ask about insights, trends, or specific queries related to the data.")

user_query = st.text_input("Ask a question about the sales data:")

if user_query:
    st.info("LLM Response Placeholder: This would be generated based on a LangChain-RAG pipeline.")
