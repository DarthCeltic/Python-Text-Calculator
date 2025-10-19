# text_calculator_v1.py
# Version 1.0 - Initial Command Line Calculator (Pre-GUI)

def calculate_text():
    """Reads a simple expression from the console and calculates it."""
    print("Welcome to the Python Text Calculator.")
    while True:
        try:
            expression = input("Enter expression (or 'quit'): ")
            if expression.lower() == 'quit':
                break
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: Invalid expression or operation. {e}")

# calculate_text()
