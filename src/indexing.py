"""Repository indexing for RAG."""

import datetime

class IndexMetadata:
    """Tracks indexing state."""

    def __init__(self):
        self.last_indexed = None
        self.file_count = 0
        self.chunk_count = 0

    def mark_indexed(self, file_count: int, chunk_count: int):
        """Mark repository as indexed."""
        self.last_indexed = datetime.datetime.now()
        self.file_count = file_count
        self.chunk_count = chunk_count
