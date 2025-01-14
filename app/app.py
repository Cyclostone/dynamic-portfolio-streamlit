import streamlit as st
from layout import load_header, load_footer
from visualizations import skill_proficiency_chart
from gemini_chatbot import GeminiChatBot
from job_match import match_skills
from content import about_section, achievements_section, chatbot_section, job_matching_section

# Page Configuration
st.set_page_config(page_title="Arpit Shrotriya Portfolio", layout="wide")

# API Keys
GEMINI_API_KEY = "AIzaSyBnPwj1Z9hMZGCsooqR4JlxlG1VCT3Tykk"
chatbot = GeminiChatBot(GEMINI_API_KEY)

# Header Section
load_header()

# About Section
st.markdown(about_section(), unsafe_allow_html=True)

# Skill Proficiency Section
with st.expander("View My Skill Proficiency", expanded=True):
    st.plotly_chart(skill_proficiency_chart(), use_container_width=True)

# Job Matching Tool Section
st.markdown(job_matching_section(), unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Job Description", type=["txt"])
if uploaded_file:
    job_description = uploaded_file.read().decode("utf-8")
    user_skills = ['Python', 'SQL', 'Machine Learning', 'Cloud Computing', 'ETL Pipelines']
    matches = match_skills(job_description, user_skills)
    st.success(f"Matching Skills: {', '.join(matches)}")

# Chatbot Section
st.markdown(chatbot_section(), unsafe_allow_html=True)
user_input = st.text_input("Type your question:")
if user_input:
    response = chatbot.respond(user_input)
    st.markdown(
        f"""
        <div style='padding: 10px; background-color: #eaf4fc; border-radius: 10px; margin-top: 10px;'>
            <p style='font-size: 1.1rem;'><strong>Response:</strong> {response}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Achievements Section
st.markdown(achievements_section(), unsafe_allow_html=True)

# Footer Section
load_footer()