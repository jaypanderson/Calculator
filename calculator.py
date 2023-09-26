"""
This is a work in progress and I intend to expand it so that I can do linear algebra as well
as statistical calculations so that I can quickly verify that my data analysis is being done
correctly.

Currently, can only perform simple arithmatic with +-/*^
"""

import customtkinter as ctk
from customtkinter import set_appearance_mode
from tkinter import *
from tkinter import END
from typing import Callable


# TODO change the whole code so that it does not rely on global variables. The code will be more verbose but it will be
# TODO explicit on what it wants to do and i can avoid using global variables and then i dont have to use a work around
# TODO with the decorator function using global variables so that i can avoid an error in compile time where the decorators
# TODO are actually called when a function is defined.
# decorator function that changes the state of the entry objects to normal while we are editing them and then
# changes it back to readonly when we are done, so that the user cannot change the entry except by using designated
# key bindings or clicking the buttons.
def temp_change_state():
    global calculation_text, current_text

    def decorator(func):
        def wrapper(*arg):
            calculation_text.configure(state="normal")
            current_text.configure(state="normal")
            try:
                result = func(*arg)
            finally:
                calculation_text.configure(state="readonly")
                current_text.configure(state="readonly")
            return result
        return wrapper
    return decorator


def change_button_status(buttons):
    if status_var.get() == "UNDEFINED":
        for button in buttons:
            button.configure(state=ctk.DISABLED)
    else:
        for button in buttons:
            button.configure(state=ctk.NORMAL)


# check to see if string is a valid float or not.
def check_if_float(num: str) -> int:
    try:
        float(num)
        return True
    except ValueError:
        return False


# add the functions to the buttons
@temp_change_state()
def button_click(number):
    print(f"Arithmatic function called with symbol: {number}")
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()

    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, str(number))
        return

    if calc_text == "":
        if cur_text == "0" or cur_text == 'UNDEFINED':
            current_text.delete(0, END)
            current_text.insert(0, str(number))
        else:
            current_text.insert(END, str(number))
        return

    if cur_text == "0":
        arith = False  # inserted to fix a potential bug when deleting operators from the calculation text.
        current_text.delete(0, END)
        current_text.insert(0, str(number))
        return
    if calc_text[-1] in "+-x÷^":
        if arith is True:
            current_text.delete(0, END)
            current_text.insert(0, str(number))
            arith = False
        else:
            current_text.insert(END, str(number))
        return
    else:
        current_text.insert(END, str(number))


@temp_change_state()
def arithmatic(symbol: str) -> None:
    print(f"Arithmatic function called with symbol: {symbol}")
    global arith, calculation_text, current_text

    calc_text = calculation_text.get()
    cur_text = current_text.get()

    if cur_text[-1:] == ".":  # added to ensure that a 0 is added to make it look better
        current_text.delete(len(cur_text) - 1, END)
        cur_text = cur_text.replace('.', '')

    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, symbol)
        arith = True
        return

    if calc_text == symbol:  # used to have cur_text == '0' or which might have been there to prevent some bug.
        arith = True
        return

    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + symbol)
    elif calc_text and calc_text[-1:] in "+-x÷^":  # calc_text is checking if it is not an empty string
        if arith is False:
            calculation_text.insert(END, cur_text + symbol)
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, symbol)
    else:
        calculation_text.insert(END, cur_text + symbol)
    arith = True


# change the last numeric values sign.
@temp_change_state()
def button_plus_minus():
    global calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if cur_text[:1] != '-' and check_if_float(cur_text) and cur_text != '0':
        current_text.insert(0, '-')
    elif cur_text[:1] == '-':
        current_text.delete(0, 1)


# TODO change is so that when an operator is press and i have 0. in the current text. it is changed back to
# TODO 0 so that it looked better, probably need to do this in the arithmatic function.
@temp_change_state()
def button_decimal():
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:] == '=':
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, '0.')
        return

    if arith is True:
        current_text.delete(0, END)
        current_text.insert(0, '0.')
        arith = False
    else:
        if '.' not in cur_text:
            current_text.insert(END, '.')
        elif '.' in cur_text and cur_text[-1] == '.':
            current_text.delete(len(cur_text) - 1, END)


@temp_change_state()
def button_clear():
    global calculation_text, current_text
    calculation_text.delete(0,  END)
    current_text.delete(0, END)
    current_text.insert(0, "0")


@temp_change_state()
def button_backspace():
    global calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if len(cur_text) == 1:
        if cur_text == "0":
            calculation_text.delete(len(calc_text) - 1, END)
        else:
            current_text.delete(0, END)
            current_text.insert(0, "0")
    else:
        current_text.delete(len(cur_text) - 1, END)


# TODO refactor code so that a good junk of the code is under the try clause. still not sure if this is best approach
# TODO or not. originally added it just to deal with zer division errors.

# TODO have to change how 0. behaves. i want it to change to 0 when ever it is inserted into the calculation text from the current text

# TODO Add way for the equal button to memorize the last operation and repeat that continuously
# TODO as long as the used keeps pressing the equals button.
# I was not able to build an eval() function that follows the order of operations.
# so I just used the built-in eval() function.
@temp_change_state()
def button_equal():
    global calculation_text, current_text, status_var
    calc_text = calculation_text.get()
    calc_text = calc_text.replace('x', '*')
    calc_text = calc_text.replace('÷', '/')
    calc_text = calc_text.replace("^", "**")  # change the ^ to ** because in python ^ is bitwise XOR operator.
    cur_text = current_text.get()

    if cur_text == "0.":  # added to ensure that a 0 is added to make it look better
        cur_text = "0"

    if calc_text[-1:] == "=":
        return

    try:
        eval(calc_text + cur_text)
    except ZeroDivisionError:
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, 'UNDEFINED')
        return

    ans = eval(calc_text + cur_text)
    if ans == int(ans):
        ans = int(ans)
    current_text.delete(0, END)
    current_text.insert(0, str(round(ans, ndigits=14)))
    calculation_text.insert(END, cur_text + "=")
    print(type(ans))
    return


def key_binds(key: Event) -> None:
    print(f"Key pressed: {key.keysym}")
    key_map = {'1': button_1,
               '2': button_2,
               '3': button_3,
               '4': button_4,
               '5': button_5,
               '6': button_6,
               '7': button_7,
               '8': button_8,
               '9': button_9,
               '0': button_0,
               '+': button_add,
               '-': button_subtract,
               '*': button_multiply,
               '/': button_divide,
               '^': button_exponential,
               '.': button_decimal}

    special_keys = {'BackSpace': button_backspace,
                    'Return': button_equal,
                    'Escape': button_clear}
    if key.char in key_map:
        func = key_map.get(key.char, None)
        func.invoke()
    elif key.keysym in special_keys:
        func = special_keys.get(key.keysym, None)
        func.invoke()


root = ctk.CTk()
root.bind("<Key>", key_binds)  # this binds the key_binds function to the CTk window.
set_appearance_mode("dark")

# this allows for different behaviors of each button depending on whether the last button was a numeric button
# or an arithmatic button such as "+-/*"
arith = False  # to check if the last entry in the calculation_text is an arithmetic operator.

root.title("Simple Calculator")
root.geometry("500x700")
root.configure(bg="lightblue")
root.resizable(True, True)  # Controls whether user can resize window.

# define font and size for buttons
button_font = ("Lucida Console", 20)

# variables to adjust button size
text_width = 400
width = int(text_width // 3.75)
height = 50
border = 1
# add buttons for the numbers
# Note: You can adjust the colors, border colors, and other properties as per your design preferences.
button_1 = ctk.CTkButton(root, text="1", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(1))
button_2 = ctk.CTkButton(root, text="2", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(2))
button_3 = ctk.CTkButton(root, text="3", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(3))
button_4 = ctk.CTkButton(root, text="4", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(4))
button_5 = ctk.CTkButton(root, text="5", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(5))
button_6 = ctk.CTkButton(root, text="6", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(6))
button_7 = ctk.CTkButton(root, text="7", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(7))
button_8 = ctk.CTkButton(root, text="8", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(8))
button_9 = ctk.CTkButton(root, text="9", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(9))
button_0 = ctk.CTkButton(root, text="0", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: button_click(0))
button_add = ctk.CTkButton(root, text="+", width=width, height=height, border_width=border, font=button_font,
                           command=lambda: arithmatic('+'))
button_subtract = ctk.CTkButton(root, text="-", width=width, height=height, border_width=border, font=button_font,
                                command=lambda: arithmatic('-'))
button_multiply = ctk.CTkButton(root, text="⨉", width=width, height=height, border_width=border, font=button_font,
                                command=lambda: arithmatic('x'))
button_divide = ctk.CTkButton(root, text="÷", width=width, height=height, border_width=border, font=button_font,
                              command=lambda: arithmatic('÷'))
button_exponential = ctk.CTkButton(root, text="^",   width=width, height=height, border_width=border, font=button_font,
                                   command=lambda: arithmatic('^'))
button_plus_minus = ctk.CTkButton(root, text="+/-",   width=width, height=height, border_width=border, font=button_font,
                                  command=button_plus_minus)
button_decimal = ctk.CTkButton(root, text=".", width=width, height=height, border_width=border, font=button_font,
                               command=button_decimal)
button_backspace = ctk.CTkButton(root, text="<-X", width=width, height=height, border_width=border, font=button_font,
                                 command=button_backspace)
button_clear = ctk.CTkButton(root, text="Clear", width=width, height=height, border_width=border, font=button_font,
                             command=button_clear)
button_equal = ctk.CTkButton(root, text="=", width=width * 2, height=height, border_width=border, font=button_font,
                             command=button_equal)


# TODO complete creating the different categories.
# organize buttons into different categories.
operators = [button_add, button_subtract, button_multiply, button_divide, button_exponential,
             button_decimal, button_plus_minus, button_backspace]


# put the buttons on the screen
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=6, column=1)
button_add.grid(row=6, column=3)
button_subtract.grid(row=5, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=3, column=3)
button_exponential.grid(row=8, column=0)
button_plus_minus.grid(row=6, column=0)
button_decimal.grid(row=6, column=2)
button_clear.grid(row=7, column=1)
button_backspace.grid(row=7, column=0)
button_equal.grid(row=7, column=2, columnspan=2)

# get the background color of the root object
root_bg_color = root.cget('bg')

# add the text box for the numbers
calculation_text = ctk.CTkEntry(root, width=text_width, fg_color=root_bg_color, border_color=root_bg_color,
                                justify="right")
calculation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
calculation_text.configure(font=("Lucida Console", 15), state="readonly")
calculation_text.bind("<Key>", lambda x: "break")

# Define a string variable that will be used to keep track if undefined is displayed on current_text or not
# in order to disable certain buttons.
status_var = ctk.StringVar()
status_var.trace_add('write', lambda *args: change_button_status(operators))  # not sure why *args makes this work

# add text box for current value
current_text = ctk.CTkEntry(root, width=text_width, textvariable=status_var, fg_color=root_bg_color,
                            border_color=root_bg_color, justify="right")
current_text.insert(0, "0")
current_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
current_text.configure(font=("Lucida Console", 30), state="readonly")


root.mainloop()
