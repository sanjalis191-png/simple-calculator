"""
Simple Calculator - Python Internship Task 1

This program performs basic arithmetic operations:
addition, subtraction, multiplication, and division.

It accepts user input, displays the result clearly,
and handles invalid input and division by zero using try/except.
"""

def calculate(num1, num2, operation):
    """Perform the selected arithmetic operation."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")


def main():
    """Run the calculator program."""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    try:
        # Take the first number from the user.
        num1 = float(input("Enter first number: "))

        # Take the second number from the user.
        num2 = float(input("Enter second number: "))

        # Ask the user which arithmetic operation to perform.
        operation = input("Enter operation (+, -, *, /): ").strip()

        # Perform the calculation.
        result = calculate(num1, num2, operation)

        # Display the result clearly.
        print("\nResult:", result)

    except ValueError as error:
        # Handles non-numeric input and invalid operations.
        if str(error) == "Invalid operation.":
            print("\nError: Please choose only +, -, * or /.")
        else:
            print("\nError: Please enter valid numbers.")

    except ZeroDivisionError:
        # Handles division by zero safely.
        print("\nError: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
