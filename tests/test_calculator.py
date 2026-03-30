# ============================================================
# tests/test_calculator.py — The Test Suite
# ============================================================
# This file is the HEART of CI/CD. Every time you push code,
# the pipeline runs these tests. If any test fails, the
# pipeline stops and tells you something is broken.
#
# Each test follows the same pattern:
#   1. Call a function with KNOWN inputs
#   2. Check that the output MATCHES what you expect
#
# pytest (our test framework) provides:
#   - Functions starting with "test_" are auto-discovered
#   - "assert" checks if something is True
#   - "pytest.raises" checks that an error is thrown
#
# RUN THIS WITH:  pytest -v
# ============================================================

import pytest
from src.calculator import (
    add, subtract, multiply, divide,
    is_even, factorial, celsius_to_fahrenheit,
)


# --- Group 1: Addition ---

class TestAdd:
    def test_two_positive_numbers(self):
        assert add(2, 3) == 5

    def test_positive_and_negative(self):
        assert add(5, -3) == 2

    def test_two_zeros(self):
        assert add(0, 0) == 0

    def test_decimal_numbers(self):
        assert add(1.5, 2.5) == 4.0


# --- Group 2: Subtraction ---

class TestSubtract:
    def test_basic_subtraction(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 7) == -4


# --- Group 3: Multiplication ---

class TestMultiply:
    def test_two_positive_numbers(self):
        assert multiply(6, 7) == 42

    def test_multiply_by_zero(self):
        assert multiply(100, 0) == 0


# --- Group 4: Division ---

class TestDivide:
    def test_even_division(self):
        assert divide(20, 4) == 5.0

    def test_decimal_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        # This test checks that your code CORRECTLY handles
        # an error case. In CI/CD, catching edge cases is critical.
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


# --- Group 5: is_even ---

class TestIsEven:
    def test_even_number(self):
        assert is_even(4) is True

    def test_odd_number(self):
        assert is_even(7) is False

    def test_zero_is_even(self):
        assert is_even(0) is True


# --- Group 6: Factorial ---

class TestFactorial:
    def test_factorial_of_five(self):
        assert factorial(5) == 120

    def test_factorial_of_zero(self):
        assert factorial(0) == 1

    def test_factorial_of_one(self):
        assert factorial(1) == 1

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-3)


# --- Group 7: Temperature conversion ---

class TestCelsiusToFahrenheit:
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_body_temperature(self):
        assert celsius_to_fahrenheit(37) == 98.6
