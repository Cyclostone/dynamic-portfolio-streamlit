import plotly.express as px
import pandas as pd

def skill_proficiency_chart():
    """Generate a radar chart for skill proficiency."""
    skills = ['Python', 'SQL', 'Machine Learning', 'Cloud Computing', 'ETL Pipelines']
    proficiency = [9, 8, 8, 7, 8]

    fig = px.line_polar(r=proficiency, theta=skills, line_close=True)
    fig.update_traces(fill='toself')
    return fig

def experience_chart():
    """Generate a bar chart showing professional experience."""
    data = pd.DataFrame({
        "Experience": ["AI Trainer", "Data Engineer", "Data Analyst"],
        "Duration (Months)": [14, 12, 4]
    })

    fig = px.bar(data, x="Experience", y="Duration (Months)", color="Experience", text="Duration (Months)")
    fig.update_traces(textposition="outside")
    return fig