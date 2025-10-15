from typing import Optional, Any

from pydantic import BaseModel
from fastapi.responses import JSONResponse


def response(data: Any, code: str = "200", message: str = "Success") -> JSONResponse:
    if data is None:
        data = {}  # ensures empty object, not null
    return JSONResponse(
        content={
            "data": data,
            "status": {
                "code": code,
                "message": message
            }
        }
    )