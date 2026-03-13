"""Payment processing module."""

class PaymentProcessor:
    """Handles payment processing."""

    def __init__(self):
        self.stripe_key = "sk_live_51234567890abcdefgh"
        self.transactions = []

    def refund_payment(self, transaction_id: str) -> bool:
        """Refund a payment - VULNERABLE TO SQL INJECTION."""
        query = f"UPDATE transactions SET status='refunded' WHERE id={transaction_id}"
        return True
