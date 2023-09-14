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
import math

# TODO change arithmatic functions so that they are not able to do anything when an error is displayed
# TODO in the calculation_text

# TODO There is a bug where if the result ends with a zero i can no longer continue with calculations. i need to reset.
# TODO if I add zero to zero it wont show up in the calculation text. it most likely has to do with the arithmatic
#      functions.


# check to see if string is a valid float or not.
def check_if_float(num: str) -> int:
    try:
        float(num)
        return True
    except ValueError:
        return False


# add the functions to the buttons
def button_click(number):
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, str(number))
        return

    if calc_text == "":
        if cur_text == "0":
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
    if calc_text[-1] in "+-*/^":
        if arith is True:
            current_text.delete(0, END)
            current_text.insert(0, str(number))
            arith = False
        else:
            current_text.insert(END, str(number))
        return
    else:
        current_text.insert(END, str(number))


def arithmatic(symbol: str) -> None:
    global arith, calculation_text, current_text

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, symbol)
        arith = True
        return
    if cur_text == "0" or calc_text == symbol:
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + symbol)
    elif calc_text and calc_text[-1:] in "+-*/^":  # calc_text is checking if it is not an empty string
        if arith is False:
            calculation_text.insert(END, current_text.get() + symbol)
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, symbol)
    else:
        calculation_text.insert(END, current_text.get() + symbol)
    arith = True


# change the last numeric values sign.
def button_plus_minus():
    global calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if cur_text[:1] != '-' and check_if_float(cur_text) and cur_text != '0':
        current_text.insert(0, '-')
    elif cur_text[:1] == '-':
        current_text.delete(0, 1)


# TODO change is so that when no number is entered into the current text after a decimal a zero
# TODO is added automatically into calculation_text to make it look better.
def button_decimal():
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if arith is True:
        current_text.delete(0, END)
        current_text.insert(0, '0.')
        arith = False
    else:
        if '.' not in cur_text:
            current_text.insert(END, '.')
        elif '.' in cur_text and cur_text[-1] == '.':
            current_text.delete(len(cur_text) - 1, END)
        elif calc_text[-1:] == '=':
            calculation_text.delete(0, END)
            current_text.delete(0, END)
            current_text.insert(0, '0.')


def button_clear():
    global calculation_text, current_text
    calculation_text.delete(0,  END)
    current_text.delete(0, END)
    current_text.insert(0, "0")


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


# TODO Add way for the equal button to memorize the last operation and repeat that continuously
# TODO as long as the used keeps pressing the equals button.
# I was not able to build an eval() function that follows the order of operations.
# so I just used the built-in eval() function.
def button_equal():
    global calculation_text, current_text
    calc_text = calculation_text.get()
    calc_text = calc_text.replace("^", "**")  # change the ^ to ** because in python ^ is bitwise XOR operator.
    cur_text = current_text.get()
    if calc_text[-1:] == "=":
        return
    ans = eval(calc_text + cur_text)
    if ans == int(ans):
        ans = int(ans)
    current_text.delete(0, END)
    current_text.insert(0, str(round(ans, ndigits=14)))
    calculation_text.insert(END, cur_text + "=")
    print(type(ans))
    return


def limit_keys(key: Event) -> None:
    allowed_keys = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "."}
    special_keys = {'BackSpace'}
    if key.char not in allowed_keys and key.keysym not in special_keys:
        return 'break'


root = ctk.CTk()
set_appearance_mode("dark")

# this allows for different behaviors of each button depending on whether the last button was a numeric button
# or an arithmatic button such as "+-/*"
arith = False  # to check if the last entry in the calculation_text is an arithmetic operator.

root.title("Simple Calculator")
root.geometry("500x700")
root.configure(bg="lightblue")
root.resizable(True, True)  # Controls whether user can resize window.


# add the text box for the numbers
text_width = 400
calculation_text = ctk.CTkEntry(root, width=text_width)
calculation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
calculation_text.configure(font=("Lucida Console", 15))
calculation_text.bind("<Key>", lambda x: "break")

# add text box for current value
current_text = ctk.CTkEntry(root, width=text_width)
current_text.insert(0, "0")
current_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
current_text.configure(font=("Lucida Console", 30))
current_text.bind("<Key>", limit_keys)  # limit input to only numeric and operator buttons


# define button font and size
button_font = ("Lucida Console", 20)

# variables to adjust button size
width = int(text_width // 3.75)
height = 50
border = 1
# add buttons for the numbers
# Note: You can adjust the colors, border colors, and other properties as per your design preferences.
button_1 = ctk.CTkButton(root, text="1", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(1))
button_2 = ctk.CTkButton(root, text="2", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(2))
button_3 = ctk.CTkButton(root, text="3", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(3))
button_4 = ctk.CTkButton(root, text="4", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(4))
button_5 = ctk.CTkButton(root, text="5", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(5))
button_6 = ctk.CTkButton(root, text="6", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(6))
button_7 = ctk.CTkButton(root, text="7", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(7))
button_8 = ctk.CTkButton(root, text="8", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(8))
button_9 = ctk.CTkButton(root, text="9", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(9))
button_0 = ctk.CTkButton(root, text="0", width=width, height=height, border_width=border, font=button_font, command=lambda: button_click(0))
button_add = ctk.CTkButton(root, text="+", width=width, height=height, border_width=border, font=button_font, command=lambda: arithmatic('+'))
button_subtract = ctk.CTkButton(root, text="-", width=width, height=height, border_width=border, font=button_font, command=lambda: arithmatic('-'))
button_multiply = ctk.CTkButton(root, text="⨉", width=width, height=height, border_width=border, font=button_font, command=lambda: arithmatic('*'))
button_divide = ctk.CTkButton(root, text="÷", width=width, height=height, border_width=border, font=button_font, command=lambda: arithmatic('/'))
button_exponential = ctk.CTkButton(root, text="^",   width=width, height=height, border_width=border, font=button_font, command=lambda: arithmatic('^'))
button_plus_minus = ctk.CTkButton(root, text="+/-",   width=width, height=height, border_width=border, font=button_font, command=button_plus_minus)
button_decimal = ctk.CTkButton(root, text=".", width=width, height=height, border_width=border, font=button_font, command=button_decimal)
button_backspace = ctk.CTkButton(root, text="<-X", width=width, height=height, border_width=border, font=button_font, command=button_backspace)
button_clear = ctk.CTkButton(root, text="Clear", width=width, height=height, border_width=border, font=button_font, command=button_clear)
button_equal = ctk.CTkButton(root, text="=", width=width * 2, height=height, border_width=border, font=button_font, command=button_equal)

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


root.mainloop()
