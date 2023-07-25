def raise_exception():
    """Raise and handle a TypeError."""
    try:
        x = "string" + 42  # This will cause a TypeError to be raised

    except TypeError:
        print("Exception raised")
