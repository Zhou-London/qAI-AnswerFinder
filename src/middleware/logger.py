"""
Middleware of registering Log
"""

from fastapi import Request
import time

async def log_request(request: Request, call_next):
    
    #To record:
    #   Request method
    #   Path
    #   Status code

    #Record requset time
    #Print request info
    start_time = time.time()
    print(f"Request started: {request.method} {request.url.path}")

    #Wait for response
    response = await call_next(request)

    #Calculate duration using response time
    #Print response info
    duration = time.time() - start_time
    print(f"Request comleted: {request.method} {request.url.path}"
          f"- Status: {response.status_code} - Time: {duration:.3f}s")
    
    return response
