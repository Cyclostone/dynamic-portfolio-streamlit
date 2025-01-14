import google.generativeai as genai

GEMINI_API_KEY = 'AIzaSyBnPwj1Z9hMZGCsooqR4JlxlG1VCT3Tykk'

class GeminiChatBot:
    
    def __init__(self, api_key, model_name="gemini-1.5-flash"):
        """
        Initialize the GeminiChatBot

        Args:
            api_key (str): API Key for Gemini
            api_url (str): The Base URL for the Gemini API

        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def respond(self, user_input):
        """
        Generate a response to the user input using the Gemini Model.

        Args:
            user_input (str): The User's Input/question.

        Returns:
            str : The chatbot's response
        
        """
        
        try:
            response = self.model.generate_content(user_input)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"