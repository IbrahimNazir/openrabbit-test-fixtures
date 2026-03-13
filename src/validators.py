"""Validators with docstring mismatch."""

def validate_user(user_id: str, email: str, age: int) -> bool:
    """Validate user.

    Args:
        user_id: User ID
        email: Email address
        (missing age in docstring!)
    """
    return user_id and email

def process_payment(amount: float) -> dict:
    """Process payment.

    Args:
        amount: Payment amount
        user_id: User making payment (NOT IN FUNCTION PARAMS!)
        currency: Currency (NOT IN FUNCTION PARAMS!)
    """
    return {"status": "success"}
