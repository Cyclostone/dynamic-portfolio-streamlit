import streamlit as st

def load_header():
    """Load the header with title and links."""
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; background-color: #1e81b0; border-radius: 10px;'>
            <h1 style='color: white; font-size: 3rem; margin-bottom: 5px;'>Arpit Shrotriya</h1>
            <p style='color: #d9faff; font-size: 1.2rem;'>👨‍💻 Data Scientist | Python | SQL | Cloud Computing</p>
            <div style='margin-top: 10px;'>
                <a href="https://github.com/Cyclostone" target="_blank" style="text-decoration: none; margin-right: 10px; padding: 10px 20px; background-color: #ffcc29; color: #1e81b0; border-radius: 5px; font-weight: bold;'>GitHub</a>
                <a href="https://medium.com/@YourMediumHandle" target="_blank" style="text-decoration: none; padding: 10px 20px; background-color: #ffcc29; color: #1e81b0; border-radius: 5px; font-weight: bold;'>Medium Blog</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def load_footer():
    """Load the footer with contact information."""
    st.markdown(
        """
        <footer style='text-align: center; padding: 10px; margin-top: 30px;'>
            <p style='font-size: 1rem;'>For collaboration or queries, email me at 
            <a href="mailto:as4893@njit.edu" style="color: #1e81b0; text-decoration: none; font-weight: bold;'>as4893@njit.edu</a></p>
        </footer>
        """,
        unsafe_allow_html=True,
    )