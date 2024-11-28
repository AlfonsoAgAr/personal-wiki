from openai import OpenAI
from chat.model import Model

class OpenAIModel(Model):
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.client = OpenAI(
            api_key=api_key
        )
        self.model = model

    def generate_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"
