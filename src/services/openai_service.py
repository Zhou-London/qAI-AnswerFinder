"""
Service of OpenAI API
1. Check whether API is available
2. Process a text
"""

from openai import OpenAI
from dotenv import load_dotenv
from services.prompts import prompt
import os

class Agent:
    def __init__(self):

        #Get key
        load_dotenv()
        openai_key = os.getenv("SECRET_KEY")
        if not openai_key:
            print("Please enter API KEY in .env file.")

        #Client
        self.client = OpenAI(api_key=openai_key)

    #Check if it is available
    def check_status(self):
        #Get response
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    #Pre-prompt
                    "role": "developer",
                    "content": prompt.pre_prompt
                },
                {
                    #Prompt
                    "role": "user",
                    "content": prompt.prompt_for_check
                }
            ],
            max_tokens=10
        )
        
        if response.choices and response.choices[0].message.content:
            return {
                "message": "Available",
                "status": "success",
                "response": response.choices[0].message.content
            }
        
        else:
            return {
                "message": "OpenAI not working",
                "status": "error",
                "response": "No response"
            }
        
    #Analyze a text
    def process_text(self,text):
        pass

openai_service = Agent()