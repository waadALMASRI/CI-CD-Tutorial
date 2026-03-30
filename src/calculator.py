# ============================================================
# src/calculator.py — A simple calculator module
# ============================================================
# This is your "application code". In a real project, this
# could be a Flask API, a Django app, a data pipeline, a CLI
# tool — anything. The key point: it has functions that can
# be imported and tested by pytest.
# ============================================================


def add(a, b):
    """Add two numbers together."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32
