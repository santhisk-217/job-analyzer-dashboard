import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# This is the list of skills you will hunt for.
# We've updated it to be more relevant to data analysis.
SKILL_KEYWORDS = [
    'python', 'sql', 'r', 'excel', 'tableau', 'power bi', 'sas',
    'spss', 'pandas', 'numpy', 'scikit-learn', 'tensorflow',
    'aws', 'azure', 'gcp', 'spark', 'hadoop', 'jira', 'agile'
]

# 1. NEW: A function to load the data from your CSV
@st.cache_data  # This caches the data so it loads instantly
def load_data():
    try:
        df = pd.read_csv("DataAnalyst.csv")
        # Clean up the 'Job Description' column
        df = df.dropna(subset=['Job Description'])
        # Clean up the 'Job Title' column
        df = df.dropna(subset=['Job Title'])
        df['Job Title'] = df['Job Title'].str.replace(r'\(.*?\)', '', regex=True).str.strip()
        return df
    except FileNotFoundError:
        st.error("Error: DataAnalyst.csv file not found.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

# 2. YOUR ORIGINAL ANALYZER (Slightly modified)
def analyze_skills(job_descriptions):
    """
    Analyzes the job descriptions for the keywords in SKILL_KEYWORDS.
    Returns a DataFrame of skill counts and a single string of all text.
    """
    # Combine all descriptions into one giant string, in lowercase
    all_text = ' '.join(job_descriptions).lower()
    
    # Count skills
    skill_counts = {skill: 0 for skill in SKILL_KEYWORDS}
    for skill in SKILL_KEYWORDS:
        # Use regex to find the skill as a whole word to avoid "r" matching "react"
        pattern = r'\b' + re.escape(skill) + r'\b'
        skill_counts[skill] = len(re.findall(pattern, all_text))
            
    # Convert to a DataFrame
    skill_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Count'])
    skill_df = skill_df[skill_df['Count'] > 0] # Keep only skills that were found
    skill_df = skill_df.sort_values(by='Count', ascending=False)
    
    return skill_df, all_text

# --- Main Streamlit App ---

st.title("📊 Job Market Analyzer")
st.markdown("Select a job title from the dataset to find the most in-demand skills.")

# Load the data
df = load_data()

# 3. NEW: A select box instead of a text input
# Get the top 30 most common job titles to keep the list clean
top_job_titles = df['Job Title'].value_counts().head(30).index.tolist()

selected_title = st.selectbox(
    "Select a Job Title:",
    options = top_job_titles
)

if st.button("Analyze Job Market"):
    if not selected_title:
        st.error("Please select a job title.")
    else:
        with st.spinner(f"Analyzing jobs for '{selected_title}'..."):
            
            # 1. Filter the DataFrame for the selected job
            filtered_df = df[df['Job Title'] == selected_title]
            
            if filtered_df.empty:
                st.error("No jobs found for that title.")
            else:
                # 2. Get the descriptions
                descriptions = filtered_df['Job Description'].tolist()
                st.success(f"Successfully found and analyzed {len(descriptions)} job descriptions!")
                
                # 3. Analyze Data
                skill_df, all_text = analyze_skills(descriptions)
                
                if skill_df.empty:
                    st.warning("No skills from your keyword list were found in the job descriptions.")
                else:
                    # 4. Display Results
                    st.subheader(f"Top In-Demand Skills for {selected_title}")
                    st.bar_chart(skill_df.head(10).set_index('Skill'))

                    st.subheader("All Found Skills (Count)")
                    st.dataframe(skill_df)
                    
                    st.subheader("Skill Word Cloud")
                    try:
                        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
                        fig, ax = plt.subplots()
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.axis("off")
                        st.pyplot(fig)
                    except ValueError:
                         st.warning("Could not generate word cloud (not enough text).")
                    except Exception as e:
                        st.error(f"Could not generate word cloud: {e}")