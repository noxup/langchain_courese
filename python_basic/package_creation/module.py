# module.py

def add(a, b):
    """
    Add two numbers and return the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The difference of the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The product of the two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    float: The quotient of the two numbers.
    
    Raises:
    ValueError: If the second number is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b