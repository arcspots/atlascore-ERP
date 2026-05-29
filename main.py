from fastapi import FastAPI
from app.core.interfaces.http.routes import company_routes, user_routes
from app.core.interfaces.http.exception_handler import domain_exception_handler
from app.core.domain.exceptions.domain_exceptions import DomainException
from app.core.interfaces.http.routes.auth_routes import router as auth_router
app = FastAPI()

print("USER ROUTER:", user_routes.router.routes)
print("COMPANY ROUTER:", company_routes.router.routes)
app.add_exception_handler(DomainException, domain_exception_handler)

app.include_router(company_routes.router)
app.include_router(user_routes.router)
app.include_router(auth_router)