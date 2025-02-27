"""
Middleware of registering Log
"""

from fastapi import Request
import time
import logging
from logging.handlers import RotatingFileHandler
import os

log_file = "src/log.log"
max_logs = 10

logger = logging.getLogger("RequestLogger")
logger.setLevel(logging.INFO)

if not logger.handlers:

    handler = RotatingFileHandler(
        log_file,
        maxBytes=1024 * 1024,
        backupCount=0,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger.addHandler(handler)

    class limited(RotatingFileHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.max_logs = max_logs

        def emit(self, record):
            if os.path.exists(self.baseFilename):
                with open(self.baseFilename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                if len(lines) >= self.max_logs:
                    with open(self.baseFilename, "w", encoding="utf-8") as f:
                        f.writelines(lines[1:])
            super().emit(record)

    logger.handlers[0] = limited(
        log_file, maxBytes=1024 * 1024, backupCount=0, encoding="utf-8"
    )
    logger.handlers[0].setFormatter(formatter)


async def log_request(request: Request, call_next):

    # Record requset time
    start_time = time.time()

    # Wait for response
    response = await call_next(request)

    # Calculate duration using response time
    duration = time.time() - start_time

    log_message = (
        f" Method: {request.method} | Path: {request.url.path} |"
        f" Status: {response.status_code} | Time: {duration:.3f}s "
    )

    logger.info(log_message)
    return response
