"""
Application
"""

from fastapi import FastAPI

#Function for middleware
import middleware
import middleware.logger

#Function for router
from routes.index import index_router
from routes.process_file import processFile_router

#Init the server
app = FastAPI()

"""
Register the middleware
"""
#app.middleware("http")(check_auth_header)
app.middleware("http")(middleware.logger.log_request)

"""
Register the route
"""
app.include_router(index_router)
app.include_router(processFile_router)