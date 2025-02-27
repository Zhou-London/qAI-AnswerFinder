"""
Models for the response of API
"""

from pydantic import BaseModel


# Model of check OpenAI availability
class api_check_response(BaseModel):
    openai: str
    yolo: str
    manticore: str
    ocr: str


# Model of process file
class processFile_response(BaseModel):
    name: str
    question: str
    answer: str
