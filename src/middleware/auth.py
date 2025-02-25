"""
Middleware of authentication
"""

from fastapi import Request, HTTPException

AUTH_KEY = "hello"


# Middleware implementation
async def check_auth_header(request: Request, call_next):
    # Get authentication header
    auth_header = request.headers.get("Authorization")
    # Check header
    if not auth_header or auth_header != AUTH_KEY:
        # Let it stop
        raise HTTPException(status_code=401, detail="Authentication Failed!")
    # Let through
    response = await call_next(request)
    return response
