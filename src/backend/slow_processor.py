"""Slow data processor - O(n²) complexity."""

class SlowProcessor:
    """Inefficient data processing."""

    def process_duplicates(self, items: list) -> list:
        """Find duplicates - O(n²) algorithm."""
        duplicates = []
        for i, item in enumerate(items):
            for j in range(i + 1, len(items)):
                if items[j] == item:
                    duplicates.append(item)
        return duplicates
