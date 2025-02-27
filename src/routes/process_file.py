"""
Route for process file page
Check OpenAI API health
"""

from fastapi import APIRouter

path = "/processFile"


# Route path
class router:

    def __init__(self):
        self.router = APIRouter()
        self._register_routes()

    # Register the route
    def _register_routes(self):

        @self.router.get(path)
        async def process_route():
            return {"path": path}


processFile_router = router().router
