from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
import os

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form.get("username"), form.get("password")

        # Simple hardcoded check for now - should be improved with hashed passwords in DB
        # User/Pass from env vars or defaults
        ADMIN_USER = os.getenv("ADMIN_USER", "admin")
        ADMIN_PASS = os.getenv("ADMIN_PASS", "admin123")

        if username == ADMIN_USER and password == ADMIN_PASS:
            request.session.update({"token": "authenticated"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        return True

authentication_backend = AdminAuth(secret_key="change-this-secret-key")
