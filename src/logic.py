"""Logic with hallucination risk."""

class PaymentLogic:
    """Complex boolean expressions."""

    def should_allow(self, verified: bool, score: float) -> bool:
        """Ambiguous logic - hard to interpret."""
        return (verified or score < 0.5) and not (score > 0.9 or not verified)

    def access_level(self, admin: bool, premium: bool, age: int) -> int:
        """Complex nested ternary - hallucination risk."""
        return 3 if admin else 2 if premium and age > 18 else 1 if premium or age > 21 else 0
