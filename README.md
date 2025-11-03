# 📊 Data Analyst Job Market Analyzer

This project is an interactive web dashboard built with Python and Streamlit. It analyzes the **DataAnalyst.csv** dataset (from Kaggle) to identify the most in-demand skills for various data-focused roles.

This app was built to demonstrate skills in data loading, data analysis (Pandas), and interactive data visualization (Streamlit).

## 🚀 Live Demo

**[Click here to view the live dashboard!]([http://localhost:8502/])**

## 📸 Screenshots

*(After you deploy it, take a screenshot of your app and drag it here!)*



## ✨ Features

* **Fast & Reliable:** Loads data instantly from a local `DataAnalyst.csv` file (using `@st.cache_data`).
* **Job Title Filtering:** Allows the user to select from the top 30 most common job titles in the dataset.
* **Skill Analysis:** Parses thousands of job descriptions to count the frequency of key technical skills (e.g., Python, SQL, Tableau).
* **Dynamic Visualizations:**
    * A **bar chart** shows the "Top 10 Most In-Demand Skills" for the selected job.
    * A **word cloud** provides a visual representation of all keywords.
    * A **data table** shows the full count for all skills found.

## 🛠️ Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas, re (Regular Expressions)
* **Web Framework / Visualization:** Streamlit
* **Plotting Libraries:** Matplotlib, WordCloud

## 💻 How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone [YOUR_GITHUB_REPO_URL_HERE]
cd [YOUR_REPO_NAME_HERE]
