"""API with broken call site."""

from src.backend.auth.service import AuthService
auth = AuthService()

def login(username: str, password: str):
    """LOGIN - BROKEN: missing mfa_code param."""
    result = auth.authenticate(username, password)
    return result
