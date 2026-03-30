# ============================================================
# main.py — Entry point of the application
# ============================================================
# Run this with: python main.py
# ============================================================

from src.calculator import (
    add, subtract, multiply, divide,
    is_even, factorial, celsius_to_fahrenheit,
)


def main():
    print("=== CI/CD Toy Project (Python) ===\n")
    print(f"  add(3, 5)                = {add(3, 5)}")
    print(f"  subtract(10, 4)          = {subtract(10, 4)}")
    print(f"  multiply(6, 7)           = {multiply(6, 7)}")
    print(f"  divide(20, 4)            = {divide(20, 4)}")
    print(f"  is_even(7)               = {is_even(7)}")
    print(f"  is_even(8)               = {is_even(8)}")
    print(f"  factorial(5)             = {factorial(5)}")
    print(f"  celsius_to_fahrenheit(0) = {celsius_to_fahrenheit(0)}")
    print("\nAll functions working!")


if __name__ == "__main__":
    main()
