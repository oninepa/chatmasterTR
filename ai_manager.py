from openai import OpenAI

class AIManager:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    def send_message(self, model, messages):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI API Error: {str(e)}")
            return None