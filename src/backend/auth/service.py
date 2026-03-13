"""Auth service with changed signature."""

class AuthService:
    """Authentication service."""

    def authenticate(self, username: str, password: str, mfa_code: str) -> dict:
        """NEW: Added mfa_code parameter."""
        return {"success": True, "mfa_verified": mfa_code == "123456"}
