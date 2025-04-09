
# Pull Request Productivity Insights Dashboard

This is a simple Streamlit app that provides insights into pull request (PR) productivity by analyzing PR data. The app allows users to upload a CSV file containing PR data and interact with an AI model (Hugging Face API) to generate productivity insights, such as:

- Dataset summary
- Bottleneck PRs
- PR merge trends
- AI-based queries for specific insights

## Features

- **Dataset Summary**: Provides an overview of the total PRs, merged PRs, and average merge time.
- **Bottleneck PRs**: Identifies PRs that took longer than average to merge.
- **PR Merge Trend**: Shows the trend of PR merges over time (grouped by week).
- **AI-based Querying**: Allows users to ask specific questions about the PR data, such as average PR merge time for a given period or identifying the developer with the most delayed PRs.

## Requirements

- Python 3.7+
- Hugging Face API Token for the AI-based queries.

### Install Dependencies

You can install all the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## How to Run the App

1. **Clone or Download the Project**:
   - If you're using Git, you can clone the repository with:

   ```bash
   git clone https://github.com/yourusername/pr-productivity-insights.git
   ```

   - Alternatively, download the project as a ZIP file and extract it.

2. **Install the Dependencies**:
   - Open a terminal or command prompt and navigate to the project directory.
   - Run the following command to install all the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Hugging Face API Token**:
   - Create a `.env` file in the root of the project directory (if it doesn't already exist).
   - Add your Hugging Face API Token to the `.env` file in the following format:

   ```bash
   HUGGINGFACE_API_TOKEN=your_huggingface_api_token
   ```

   - If you don't have an API token yet, create an account at [Hugging Face](https://huggingface.co/) and generate an API token [here](https://huggingface.co/settings/tokens).

4. **Run the Streamlit App**:
   - In the terminal, while in the project directory, run the following command to start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. **Open the App**:
   - Once the app is running, Streamlit will provide a URL (usually `http://localhost:8501`) in the terminal.
   - Open the URL in your web browser to access the app.

6. **Upload the Dataset**:
   - The app will ask you to upload a CSV file. Ensure your dataset contains the necessary columns (PR_ID, Created_Date, Merged_Date, Assignee, Status, Reviewer_Feedback).
   - The app will process your data and display various insights, such as the dataset summary, bottleneck PRs, PR merge trend, and allow you to ask specific AI-based queries.

---

Enjoy using the Pull Request Productivity Insights Dashboard! If you encounter any issues or have any questions, feel free to open an issue on GitHub or contact me directly.

## Example Dataset Format

Ensure your CSV dataset contains the following columns:

| PR_ID | Created_Date          | Merged_Date           | Assignee | Status | Reviewer_Feedback |
|-------|-----------------------|-----------------------|----------|--------|-------------------|
| 1     | 2024-12-17 07:15:08   | 2024-12-21 07:15:08   | Bob      | merged | Pending review    |
| 2     | 2025-01-12 07:15:08   | 2025-01-17 07:15:08   | Eve      | closed | Good              |
| 3     | 2025-01-21 07:15:08   |                       | Alice    | open   | Good              |
| ...   | ...                   | ...                   | ...      | ...    | ...               |

Make sure the `Created_Date` and `Merged_Date` are in `YYYY-MM-DD HH:MM:SS` format.

## Troubleshooting

- **API Token Error**: Ensure that your Hugging Face API Token is correctly set in the `.env` file and that the token is active.
- **Missing Columns**: Make sure the CSV file contains the necessary columns (`PR_ID`, `Created_Date`, `Merged_Date`, `Assignee`, `Status`, `Reviewer_Feedback`).

Feel free to open an issue on GitHub if you encounter any problems!
```

