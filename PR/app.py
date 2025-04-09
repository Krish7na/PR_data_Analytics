import streamlit as st
import pandas as pd
from pr_analysis import (
    generate_dataset_summary,
    identify_bottlenecks,
    analyze_trend,
    answer_user_query
)

st.set_page_config(page_title="PR Productivity Insights", layout="wide")
st.title("🔍 Pull Request Productivity Insights Dashboard")

uploaded_file = st.file_uploader("📁 Upload PR Dataset CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.header("📋 Dataset Summary")
    summary = generate_dataset_summary(df)
    st.markdown(summary)

    st.header("🚨 Bottleneck PRs")
    try:
        bottlenecks = identify_bottlenecks(df)
        st.dataframe(bottlenecks)
    except Exception as e:
        st.error(f"⚠️ Could not calculate bottlenecks: {e}")

    st.header("📈 PR Merge Trend (by Week)")
    try:
        trend = analyze_trend(df)
        st.line_chart(trend.set_index('week'))
    except Exception as e:
        st.error(f"⚠️ Could not generate trend chart: {e}")

    st.header("🤖 Ask an AI Question")
    user_question = st.text_input("E.g., What is the average PR merge time for last month?")
    if user_question:
        with st.spinner("Thinking..."):
            response = answer_user_query(user_question, df)
        st.markdown(response)