def my_function():
    """ Demonstrates triple double quotes 
        docstring and does nothing raley.
    """
    return None
print("Using __doc__:")
print(my_function.__doc__)
print("Using help:")
help(my_function)