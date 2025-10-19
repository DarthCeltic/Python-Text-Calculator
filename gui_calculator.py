# gui_calculator.py
#
# Work Item: Week 2 - Implementation of a Graphical User Interface (GUI) and Exponentiation Feature (x^y).
#
# This file transitions the project from a command-line interface to a modern, event-driven
# GUI using the built-in Tkinter library.

import tkinter as tk
from tkinter import font
import math

class CalculatorGUI:
def **init**(self, master):
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

# Define the button layout for Week 2 (basic functions, trig, and exponent)
buttons = [
    # Row 1 (Trig functions and clear)
    ('sin', 1, 0, self.op_scientific_prefix), ('cos', 1, 1, self.op_scientific_prefix), ('tan', 1, 2, self.op_scientific_prefix),
    ('AC', 1, 3, self.clear_all), ('DEL', 1, 4, self.backspace),

    # Row 2
    ('7', 2, 0, self.button_click), ('8', 2, 1, self.button_click), ('9', 2, 2, self.button_click),
    ('/', 2, 3, self.button_click), ('x^y', 2, 4, self.op_exponent), # New Exponentiation

    # Row 3
    ('4', 3, 0, self.button_click), ('5', 3, 1, self.button_click), ('6', 3, 2, self.button_click),
    ('*', 3, 3, self.button_click), ('log', 3, 4, self.op_scientific_prefix),

    # Row 4
    ('1', 4, 0, self.button_click), ('2', 4, 1, self.button_click), ('3', 4, 2, self.button_click),
    ('-', 4, 3, self.button_click), ('(', 4, 4, self.button_click),

    # Row 5
    ('0', 5, 0, self.button_click), ('.', 5, 1, self.button_click), ('=', 5, 2, self.calculate), 
    ('+', 5, 3, self.button_click), (')', 5, 4, self.button_click)
]

# Create the buttons
for (text, row, col, command) in buttons:
    self.create_button(text, row, col, command)

# Configure grid weights for responsiveness
master.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
master.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
def create_button(self, text, row, col, command): """Helper function to create styled buttons.""" is_operator_or_func = text in ('+', '-', '*', '/', 'AC', 'DEL', '=', 'x^y') or text.isalpha() bg_color = "#34495e" if is_operator_or_func else "#ecf0f1" fg_color = "#e74c3c" if text in ('AC', 'DEL') else ("white" if is_operator_or_func else "#2c3e50")

button = tk.Button(
    self.master, text=text, padx=20, pady=20, font=self.default_font, bd=1, relief=tk.RAISED,
    bg=bg_color, fg=fg_color, activebackground="#bdc3c7", 
    command=lambda: command(text)
)
button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
--- Interaction Methods ---
def button_click(self, char): self.current_expression += str(char) self.input_text.set(self.current_expression)

def clear_all(self, _=None): self.current_expression = "" self.input_text.set("")

def backspace(self, _=None): self.current_expression = self.current_expression[:-1] self.input_text.set(self.current_expression)

def op_exponent(self, _=None): """Maps the x^y button to Python's '' operator.""" self.current_expression += "" self.input_text.set(self.current_expression)

def op_scientific_prefix(self, op): """Handles trigonometric and log functions.""" # Simple implementation using eval requires explicit 'math.' prefix op_map = {'sin': 'math.sin', 'cos': 'math.cos', 'tan': 'math.tan', 'log': 'math.log'} python_op = op_map.get(op) self.current_expression += f"{python_op}(" self.input_text.set(self.current_expression)

def calculate(self, _=None): """Evaluates the expression and handles errors.""" try: current_expr_clean = self.current_expression result = eval(current_expr_clean)

    self.input_text.set(str(result))
    self.current_expression = str(result)
except ZeroDivisionError:
    self.input_text.set("Error: Div by Zero")
    self.current_expression = ""
except SyntaxError:
    self.input_text.set("Error: Invalid Input")
    self.current_expression = ""
except Exception as e:
    self.input_text.set("Error")
    self.current_expression = ""

if **name** == "**main**":
\# Main application setup
root = tk.Tk()
root.configure(bg="\#2c3e50")

screen_width = root.winfo_screenwidth() screen_height = root.winfo_screenheight() window_width = 400 window_height = 500 x_cordinate = int((screen_width/2) - (window_width/2)) y_cordinate = int((screen_height/2) - (window_height/2)) root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}") root.resizable(True, True)

calc_app = CalculatorGUI(root) root.mainloop()
