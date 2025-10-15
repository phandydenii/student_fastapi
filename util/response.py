from fastapi.responses import JSONResponse
from typing import Any, Optional
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")  # Type of the data

class Status(BaseModel,Generic[T]):
    code: str
    message: str

class ResponseSchema(BaseModel, Generic[T]):
    data: Optional[T]
    status: Status

def response(
    data: Optional[Any] = None,
    code: str = "200",
    message: str = "Success"
) -> JSONResponse:
    """
    Standardized API response format:
    {
        "data": ...,
        "status": {
            "code": "...",
            "message": "..."
        }
    }
    """
    if data is None:
        data = {}  # ensures empty object instead of null

    return JSONResponse(
        content={
            "data": data,
            "status": {
                "code": code,
                "message": message
            }
        }
    )


# Optional: Shortcut helpers for common response codes

def success(data: Any = None, message: str = "Success") -> JSONResponse:
    return response(data=data, code="200", message=message)

def created(data: Any = None, message: str = "Created successfully") -> JSONResponse:
    return response(data=data, code="201", message=message)

def bad_request(message: str = "Bad request") -> JSONResponse:
    return response(data={}, code="400", message=message)

def unauthorized(message: str = "Unauthorized") -> JSONResponse:
    return response(data={}, code="401", message=message)

def forbidden(message: str = "Forbidden") -> JSONResponse:
    return response(data={}, code="403", message=message)

def not_found(message: str = "Not found") -> JSONResponse:
    return response(data={}, code="404", message=message)

def internal_error(message: str = "Internal server error") -> JSONResponse:
    return response(data={}, code="500", message=message)
