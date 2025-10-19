# gui_calculator.py
#
# Work Item: Week 3 - Implementation of Square Root, Factorial, Modulus, and Pi Constant.
#
# This update expands the calculator's scientific functionality, adjusts the button
# layout to accommodate new operations, and refines error handling.

import tkinter as tk
from tkinter import font
import math

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        
        # Configure fonts
        self.default_font = font.Font(family="Arial", size=14)
        self.display_font = font.Font(family="Arial", size=24, weight="bold")
        
        self.current_expression = ""
        self.input_text = tk.StringVar()

        # Display Widget
        self.display = tk.Entry(
            master,
            textvariable=self.input_text,
            font=self.display_font,
            bd=5,
            relief=tk.SUNKEN,
            justify='right',
            state='readonly',
            readonlybackground="#2c3e50", 
            fg="white"
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Define the button layout and functions (Expanded for Week 3 features)
        buttons = [
            # Row 1 (Advanced Functions and Constants)
            ('sqrt', 1, 0, self.op_scientific_prefix), ('!', 1, 1, self.op_scientific_prefix), ('Mod', 1, 2, self.op_modulus),
            ('AC', 1, 3, self.clear_all), ('DEL', 1, 4, self.backspace),
            
            # Row 2 (Trigonometric functions and Exponent)
            ('sin', 2, 0, self.op_scientific_prefix), ('cos', 2, 1, self.op_scientific_prefix), ('tan', 2, 2, self.op_scientific_prefix),
            ('log', 2, 3, self.op_scientific_prefix), ('x^y', 2, 4, self.op_exponent), 
            
            # Row 3 (Numbers 7-9 and basic operators)
            ('7', 3, 0, self.button_click), ('8', 3, 1, self.button_click), ('9', 3, 2, self.button_click),
            ('/', 3, 3, self.button_click), ('*', 3, 4, self.button_click),
            
            # Row 4 (Numbers 4-6 and basic operators)
            ('4', 4, 0, self.button_click), ('5', 4, 1, self.button_click), ('6', 4, 2, self.button_click),
            ('-', 4, 3, self.button_click), ('+', 4, 4, self.button_click),
            
            # Row 5 (Numbers 1-3, constants, and parentheses)
            ('1', 5, 0, self.button_click), ('2', 5, 1, self.button_click), ('3', 5, 2, self.button_click),
            ('(', 5, 3, self.button_click), (')', 5, 4, self.button_click),
            
            # Row 6 (Bottom row: 0, decimal, pi, equals)
            ('0', 6, 0, self.button_click), ('.', 6, 1, self.button_click), ('π', 6, 2, self.op_constant),
            ('=', 6, 3, self.calculate), ('e', 6, 4, self.op_constant) 
        ]

        # Create the buttons and configure grid weights
        for (text, row, col, command) in buttons:
            self.create_button(text, row, col, command)
            
        master.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        master.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        
    def create_button(self, text, row, col, command):
        """Helper function to create styled buttons."""
        is_operator_or_func = text in ('+', '-', '*', '/', 'AC', 'DEL', '=', 'x^y', 'sqrt', '!', 'Mod') or text.isalpha()
        is_constant = text in ('π', 'e')

        bg_color = "#34495e" if is_operator_or_func else "#ecf0f1"
        if is_constant: bg_color = "#16a085" # Teal for constants
        
        fg_color = "#e74c3c" if text in ('AC', 'DEL') else ("white" if is_operator_or_func or is_constant else "#2c3e50")
        
        button = tk.Button(
            self.master, text=text, padx=20, pady=20, font=self.default_font, bd=1, relief=tk.RAISED,
            bg=bg_color, fg=fg_color, activebackground="#bdc3c7", 
            command=lambda: command(text)
        )
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

    def button_click(self, char):
        self.current_expression += str(char)
        self.input_text.set(self.current_expression)

    def clear_all(self, _=None):
        self.current_expression = ""
        self.input_text.set("")
        
    def backspace(self, _=None):
        self.current_expression = self.current_expression[:-1]
        self.input_text.set(self.current_expression)

    def op_exponent(self, _=None):
        self.current_expression += "**"
        self.input_text.set(self.current_expression)
        
    def op_modulus(self, _=None):
        """Handles the Modulus feature (Mod)."""
        self.current_expression += "%"
        self.input_text.set(self.current_expression)

    def op_constant(self, const_name):
        """Handles insertion of mathematical constants (pi, e)."""
        if const_name == 'π':
            self.current_expression += str(math.pi)
        elif const_name == 'e':
            self.current_expression += str(math.e)
        self.input_text.set(self.current_expression)
        
    def op_scientific_prefix(self, op):
        """Handles trigonometric, log, sqrt, and factorial functions."""
        # Map button text to the actual Python function call
        op_map = {
            'sin': 'math.sin', 'cos': 'math.cos', 'tan': 'math.tan',
            'log': 'math.log', 'sqrt': 'math.sqrt', '!': 'math.factorial'
        }
        
        python_op = op_map.get(op)
        self.current_expression += f"{python_op}("
        self.input_text.set(self.current_expression)


    def calculate(self, _=None):
        """Evaluates the mathematical expression and handles errors."""
        try:
            # Substitute constants and evaluate
            current_expr_clean = self.current_expression.replace('π', str(math.pi)).replace('e', str(math.e))
            result = eval(current_expr_clean)
            
            self.input_text.set(str(result))
            self.current_expression = str(result)
        except ZeroDivisionError:
            self.input_text.set("Error: Div by Zero")
            self.current_expression = ""
        except ValueError:
            self.input_text.set("Error: Invalid Value (e.g. sqrt(-1))")
            self.current_expression = ""
        except SyntaxError:
            self.input_text.set("Error: Invalid Input")
            self.current_expression = ""
        except Exception as e:
            self.input_text.set("Error")
            self.current_expression = ""


if __name__ == "__main__":
    # Main application setup
    root = tk.Tk()
    root.configure(bg="#2c3e50") 
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 550 # Increased height for the new row
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    root.resizable(True, True) 
    
    calc_app = CalculatorGUI(root)
    root.mainloop()
