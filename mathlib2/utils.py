def is_number(value):
    """Check if the value is a number."""
    return isinstance(value, (int, float))


def validate_input(*args):
    """Ensure all inputs are valid numbers."""
    for arg in args:
        if not is_number(arg):
            raise ValueError(f"Invalid input: {arg} is not a number.")