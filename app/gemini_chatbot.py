import google.generativeai as genai
import PyPDF2

class CustomGeminiChatBot:
    def __init__(self, api_key, model_name="gemini-1.5-flash", resume_path=None, linkedin_url=None):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.resume_text = self._parse_resume(resume_path) if resume_path else ""
        self.linkedin_url = linkedin_url

    def _parse_resume(self, resume_path):
        """Extract text from the resume PDF."""
        try:
            with open(resume_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"Error reading resume: {str(e)}"

    def generate_context(self):
        """Generate context for the chatbot."""
        context = "This chatbot answers questions about Arpit Shrotriya's professional background.\n\n"
        context += f"Resume:\n{self.resume_text[:1000]}\n\n"  # Include a snippet of the resume
        context += f"LinkedIn Profile: {self.linkedin_url}\n"
        return context

    def respond(self, user_input):
        """Generate a response from the Gemini model."""
        try:
            # Prepend context to the user input
            context = self.generate_context()
            prompt = f"{context}\nUser: {user_input}\nBot:"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"