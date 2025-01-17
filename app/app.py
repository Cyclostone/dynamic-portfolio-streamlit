import streamlit as st
from layout import load_header, load_footer
from visualizations import skill_proficiency_chart, experience_chart
from gemini_chatbot import CustomGeminiChatBot
from content import about_section, achievements_section, chatbot_section, job_matching_section

# Page Configuration
st.set_page_config(page_title="Arpit Shrotriya Portfolio", layout="wide")

# API Keys
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
RESUME_PATH = "assets/Arpit_Shrotriya_CV.pdf"
LINKEDIN_URL = "https://www.linkedin.com/in/arpit-shrotriya/"

# Chatbot
chatbot = CustomGeminiChatBot(api_key=GEMINI_API_KEY, resume_path=RESUME_PATH, linkedin_url=LINKEDIN_URL)

# Load UI Components
load_header()

# About Me Section
st.markdown(about_section(), unsafe_allow_html=True)

# Visualizations
st.markdown("### Skill Proficiency")
st.plotly_chart(skill_proficiency_chart(), use_container_width=True)

st.markdown("### Professional Experience")
st.plotly_chart(experience_chart(), use_container_width=True)

# Chatbot Section
st.markdown("## Ask Me About My Work!")
user_input = st.text_input("Type your question:")
if user_input:
    st.write(chatbot.respond(user_input))

# Footer
load_footer()