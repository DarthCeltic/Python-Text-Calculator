# calculator.py

# Import all necessary functions from other files
from Factorial import factorial
from Area import area_of_square, area_of_circle, area_of_triangle, area_of_rectangle
from Volume import volume_of_cube, volume_of_cuboid, volume_of_cylinder, volume_of_sphere, volume_of_cone

def Calculator():
    """A simple calculator program that performs various calculations."""
    while True:
        print("-" * 30)
        calc = input("What kind of calculation do you wish to do? (type ? for help): ")

        # Exit the program
        if calc == "exit":
            print("Thank you for using the calculator. Goodbye!")
            break

        # Display help menu
        elif calc == "?":
            print("\nSupported: *, /, +, -, %, sq, fact, area, vol")

        # Handle supported calculations
        elif calc in ["*", "/", "+", "-", "%", "sq", "fact"]:
            try:
                if calc == "fact":
                    num = int(input("Please enter the number for factorial: "))
                    print(f"Answer: {factorial(num)}")
                
                elif calc == "sq":
                    num = float(input("Please enter the number to square: "))
                    print(f"Answer: {num ** 2}")
                else:
                    num1 = float(input("Please enter the first number: "))
                    num2 = float(input("Please enter the second number: "))
                    
                    if calc == "*":
                        print(f"Answer: {num1 * num2}")
                    elif calc == "/":
                        if num2 == 0:
                            print("Error: Cannot divide by zero.")
                        else:
                            print(f"Answer: {num1 / num2}")
                    elif calc == "+":
                        print(f"Answer: {num1 + num2}")
                    elif calc == "-":
                        print(f"Answer: {num1 - num2}")
                    elif calc == "%":
                        if num2 == 0:
                            print("Error: Cannot perform modulo with zero.")
                        else:
                            print(f"Answer: {num1 % num2}")

            except ValueError:
                print("Invalid input. Please enter a number.")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        
        # Handle Area calculations
        elif calc == "area":
            try:
                shape = input("Area of what? (circle, square, triangle, rectangle): ")
                if shape == "circle":
                    radius = float(input("Enter the radius: "))
                    print(f"Answer: {area_of_circle(radius)}")
                elif shape == "square":
                    side = float(input("Enter the side length: "))
                    print(f"Answer: {area_of_square(side)}")
                elif shape == "triangle":
                    base = float(input("Enter the base: "))
                    height = float(input("Enter the height: "))
                    print(f"Answer: {area_of_triangle(base, height)}")
                elif shape == "rectangle":
                    length = float(input("Enter the length: "))
                    width = float(input("Enter the width: "))
                    print(f"Answer: {area_of_rectangle(length, width)}")
                else:
                    print("Invalid shape.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Handle Volume calculations
        elif calc == "vol":
            try:
                shape = input("Volume of what? (cube, cuboid, cylinder, sphere, cone): ")
                if shape == "cube":
                    side = float(input("Enter the side length: "))
                    print(f"Answer: {volume_of_cube(side)}")
                elif shape == "cuboid":
                    length = float(input("Enter the length: "))
                    width = float(input("Enter the width: "))
                    height = float(input("Enter the height: "))
                    print(f"Answer: {volume_of_cuboid(length, width, height)}")
                elif shape == "cylinder":
                    radius = float(input("Enter the radius: "))
                    height = float(input("Enter the height: "))
                    print(f"Answer: {volume_of_cylinder(radius, height)}")
                elif shape == "sphere":
                    radius = float(input("Enter the radius: "))
                    print(f"Answer: {volume_of_sphere(radius)}")
                elif shape == "cone":
                    radius = float(input("Enter the radius: "))
                    height = float(input("Enter the height: "))
                    print(f"Answer: {volume_of_cone(radius, height)}")
                else:
                    print("Invalid shape.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Handle unsupported calculations
        else:
            print("\nSorry, I don't understand your request.")
            print("Supported calculations are: *, /, +, -, sq, %, fact, area, and vol.")

# Start the calculator
if __name__ == "__main__":
    print("\nWelcome to the Python Calculator!")
    Calculator()