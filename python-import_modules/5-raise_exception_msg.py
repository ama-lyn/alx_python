def raise_exception_msg(message=""):
    """Raise a TypeError."""
    raise NameError(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print("Exception has been raised")
