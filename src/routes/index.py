"""
Route for index page
Check OpenAI API health
"""

from fastapi import APIRouter
from models.response_model import api_check_response
from services.openai_service import openai_service

#Routing path
path = '/'

class router:

    def __init__(self):
        self.router = APIRouter()
        self._register_routes()

    #Register the route.
    #And check API availbility
    def _register_routes(self):

        @self.router.get(path, response_model=api_check_response)
        async def index_route():

            json = self.get_response()

            return json
        
    #Helper function to check API availbility
    def get_response(self):
        return openai_service.check_status()


index_router = router().router