import pandas as pd
from llm_utils import query_huggingface

def generate_dataset_summary(df):
    df.columns = df.columns.str.strip().str.lower()
    required_columns = ['created_date', 'merged_date', 'status']
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        return f"❌ Missing required columns: {missing}"

    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['merged_date'] = pd.to_datetime(df['merged_date'], errors='coerce')

    total_prs = len(df)
    merged_prs = df[df['status'].str.lower() == 'merged']
    avg_merge_time = (merged_prs['merged_date'] - merged_prs['created_date']).mean()

    return f"""
✅ Total PRs: {total_prs}  
✅ Merged PRs: {len(merged_prs)}  
⏱ Average Merge Time: {avg_merge_time}
"""

def identify_bottlenecks(df):
    df.columns = df.columns.str.strip().str.lower()
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['merged_date'] = pd.to_datetime(df['merged_date'], errors='coerce')

    merged_prs = df[df['status'].str.lower() == 'merged'].copy()
    merged_prs['merge_duration'] = (merged_prs['merged_date'] - merged_prs['created_date']).dt.days
    avg_duration = merged_prs['merge_duration'].mean()

    bottlenecks = merged_prs[merged_prs['merge_duration'] > avg_duration]
    return bottlenecks[['created_date', 'merged_date', 'assignee', 'merge_duration', 'reviewer_feedback']]

def analyze_trend(df):
    df.columns = df.columns.str.strip().str.lower()
    df['merged_date'] = pd.to_datetime(df['merged_date'], errors='coerce')
    df = df[df['status'].str.lower() == 'merged']
    df['week'] = df['merged_date'].dt.to_period('W')

    trend = df.groupby('week').size().reset_index(name='merged_prs')
    return trend

def answer_user_query(question, df):
    import json
    from llm_utils import query_huggingface

    df.columns = df.columns.str.strip().str.lower()
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['merged_date'] = pd.to_datetime(df['merged_date'], errors='coerce')

    # Convert datetime columns to ISO format strings
    df['created_date'] = df['created_date'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)
    df['merged_date'] = df['merged_date'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)

    data_sample = df.to_dict(orient='records')

    prompt = f"""
You are a helpful PR data analysis assistant. Analyze this pull request dataset and answer the question concisely.

PR Data:
{json.dumps(data_sample)}

Question: {question}

Just give a direct answer to the question with no explanation or code.
Answer:"""

    return query_huggingface(prompt)