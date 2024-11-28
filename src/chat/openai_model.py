import openai
from chat.model import Model

class OpenAIModel(Model):
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def generate_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            return f"Error: {str(e)}"
