"""
Service of OpenAI API
1. Check whether API is available
2. Process a text
"""

from openai import OpenAI
from dotenv import load_dotenv
from services.prompts import prompt
import os

MODEL = "gpt-4o"


class Agent:
    def __init__(self):

        # Get key
        load_dotenv()
        openai_key = os.getenv("SECRET_KEY")

        if not openai_key:
            print("Please enter API KEY in .env file.")
        # Client
        self.client = OpenAI(api_key=openai_key)
        self.model = MODEL

    # Check if it is available
    def check_status(self):
        # Get response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    # Pre-prompt
                    "role": "developer",
                    "content": prompt.pre_prompt,
                },
                {
                    # Prompt
                    "role": "user",
                    "content": prompt.prompt_for_check,
                },
            ],
            max_tokens=10,
        )

        # Available
        if response.choices and response.choices[0].message.content:
            return True

        # Not Available
        else:
            return False

    # Analyze a text
    def process_text(self, text):
        pass


openai_service = Agent()
