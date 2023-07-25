def raise_exception():
    """Raise a TypeError."""
    x = "string" + 42  # This will cause a TypeError to be raised


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception has been raised")
