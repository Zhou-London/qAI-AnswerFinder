"""
Models for the response of API
"""

from pydantic import BaseModel

class api_check_response(BaseModel):
    message: str
    status: str
    response: str | None

class processFile_response(BaseModel):
    name: str
    question: str
    answer: str
