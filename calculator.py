# For now, just a simple Calculator
# Creator: MisterNSA aka Tobias Dominik Weber
# Date: 18.11.2020 Version 1.0
# Update Plans: Adding more functionality like powers, square roots etc.

import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Calculator")

""" Variables: 
string - Expressions - Holds all the numbers and operators the user inputs. Used for the Backend.
text_shown - string - The current output GUI shows to the User. Same as the expression, but used for the frontend.
"""
expressions = ""
text_shown = tk.StringVar()

# ---- functionality ----


def on_press(num):
    """Ads the Number or operator to the Calculators 'Memory'/ the expressions"""
    global expressions
    expressions += str(num)
    text_shown.set(expressions)


def clear():
    """Clears the Calculators 'Memory'/ the expressions and sets the shown text equals to the cleared expressions"""
    global expressions
    expressions = ""
    text_shown.set(expressions)


def equal():
    """Solves the given mathematical operation and shows the result"""
    global expressions
    expressions = str(eval(expressions))
    text_shown.set(expressions)


# text should start at the right | textvariable can Change
entry = ttk.Entry(win, justify="right", textvariable=text_shown)
entry.grid(row=0, columnspan=4, sticky="nesw")

# ----- buttons -----
# row1
button_7 = ttk.Button(win, text="7", command=lambda: on_press(7))
button_7.grid(row=1, column=0)

button_8 = ttk.Button(win, text="8", command=lambda: on_press(8))
button_8.grid(row=1, column=1)

button_9 = ttk.Button(win, text="9", command=lambda: on_press(9))
button_9.grid(row=1, column=2)

button_divide = ttk.Button(win, text="/", command=lambda: on_press("/"))
button_divide.grid(row=1, column=3)

# row2
button_4 = ttk.Button(win, text="4", command=lambda: on_press(4))
button_4.grid(row=2, column=0)

button_5 = ttk.Button(win, text="5", command=lambda: on_press(5))
button_5.grid(row=2, column=1)

button_6 = ttk.Button(win, text="6", command=lambda: on_press(6))
button_6.grid(row=2, column=2)

button_multiply = ttk.Button(win, text="*", command=lambda: on_press("*"))
button_multiply.grid(row=2, column=3)

# row3
button_1 = ttk.Button(win, text="1", command=lambda: on_press(1))
button_1.grid(row=3, column=0)

button_2 = ttk.Button(win, text="2", command=lambda: on_press(2))
button_2.grid(row=3, column=1)

button_3 = ttk.Button(win, text="3", command=lambda: on_press(3))
button_3.grid(row=3, column=2)

button_subtract = ttk.Button(win, text="-", command=lambda: on_press("-"))
button_subtract.grid(row=3, column=3)

# row4
button_0 = ttk.Button(win, text="0", command=lambda: on_press(0))
button_0.grid(row=4, column=0)

button_dot = ttk.Button(win, text=".", command=lambda: on_press("."))
button_dot.grid(row=4, column=1)

button_clear = ttk.Button(win, text="clear", command=clear)
button_clear.grid(row=4, column=2)

button_add = ttk.Button(win, text="+", command=lambda: on_press("+"))
button_add.grid(row=4, column=3)

# row5
button_equals = ttk.Button(win, text="=", command=equal)
# place in middle of the4 colums and stretch to north, east, south, west
button_equals.grid(row=5, columnspan=4, sticky="nesw")


win.mainloop()
