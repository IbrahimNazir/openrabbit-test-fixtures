"""Utility functions - candidates for refactoring."""

def load_config(config_file: str) -> dict:
    """Load config from file."""
    with open(config_file) as f:
        config = {}
        for line in f:
            key, value = line.strip().split("=")
            config[key.strip()] = value.strip()
        return config

def validate_required_fields(obj: dict) -> bool:
    """Validate required fields - should use all()."""
    is_valid = True
    for key in ["host", "port", "user"]:
        if key not in obj or not obj[key]:
            is_valid = False
    return is_valid
