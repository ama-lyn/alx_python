def raise_and_handle_type_exception():
    """Raise and handle a TypeError."""
    try:
        x = "string" + 42  # This will cause a TypeError to be raised
    except TypeError as e:
        print("Exception has been raised")
