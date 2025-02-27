"""
Route for index page
Check OpenAI API health
"""

from fastapi import APIRouter
from models.response_model import api_check_response
from services.openai_service import openai_service
from services.yolo_service import yolo_service
from services.manticore_service import manticore_service

# Routing path
path = "/"


class router:

    def __init__(self):
        self.router = APIRouter()
        self._register_routes()

    # Register the route.
    def _register_routes(self):

        @self.router.get(path, response_model=api_check_response)
        async def index_route():

            # Check API availability
            return self.check_avail()

    # Check API availability
    def check_avail(self):
        openai_avail = openai_service.check_status()
        yolo_avail = yolo_service.check_status()
        manticore_avail = manticore_service.check_status()
        ocr_avail = None

        json = {
            "openai": f"{openai_avail}. {openai_service.model}",
            "yolo": f"{yolo_avail}. YOLO11-l",
            "manticore": f"{manticore_avail}.",
            "ocr": f"{ocr_avail}.",
        }

        return json


index_router = router().router
