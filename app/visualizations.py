import plotly.express as px

def skill_proficiency_chart():
    skills = ['Python', 'SQL', 'Machine Learning', 'Cloud Computing', 'ETL Pipelines']
    proficiency = [9, 8, 8, 7, 8]

    fig = px.line_polar(r=proficiency, theta=skills, line_close=True)
    fig.update_traces(fill='toself')
    return fig