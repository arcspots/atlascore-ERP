from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.domain.exceptions.domain_exceptions import DomainException


async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Business Rule Violation",
            "message": str(exc)
        }
    )