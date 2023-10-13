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
# Callable is for when a function is returned as its return value
from typing import Callable

# TODO add a history feature that records the calculation and an answer in a different text box.

# TODO add documentation for all the functions

# TODO add type hinting for all the functions

# TODO make changes so that the my code only runs if this is __main__, that is add if __name__ == '__main__' clause.

# TODO create unit test that works with this code.

# TODO add two parentheses buttons, one to open ( and one to close ).  make sure these buttons are able to keep track
# TODO of how many open parentheses there are. that is anytime ( is pressed ad 1 to a counter and every time ) is
# TODO is press subtract 1 from the count.  It would be best if I could display that on the button but if not an
# TODO internal counter will work just fine.

# TODO change the whole code so that it does not rely on global variables. The code will be more verbose but it will be
# TODO explicit on what it wants to do and i can avoid using global variables and then i dont have to use a work around
# TODO with the decorator function using global variables so that i can avoid an error in compile time where the
# TODO decorators are actually called when a function is defined.

# TODO add functionality to calculator so that when two or more numbers are in the calulation_text and then add a second
# TODO operator such like this '9x3+' the result of the answer so far appears in the current text so for this case
# TODO current_text would be '27'

# Decorator function to change the state of entry objects.
def temp_change_state() -> Callable:
    """
    A decorator function that will be applied to most of the functions relating to button inputs.  The Entry objects
    are set up in a way that they are readonly and the user can not type into them directly.  Only when a button is
    pressed can the entry object texts change.  When ever a function with this decorator is invoked it enables the entry
    objects to normal, the functions then change the text through the operations, then finally it changes the state back
    to read only.  Global variables are being used to avoid invocation during evaluation by the interpreter because I
    want to  keep these variables close to the entry UI elements of the script for organization.
    :return: return the wrapped function.
    """
    global calculation_text, current_text

    def decorator(func: Callable) -> Callable:
        def wrapper(*arg: ctk.CTkEntry) -> Callable:
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


# decorator function to set the global variable of arith
def change_arith(val: bool) -> Callable:
    """
    A decorator function to simplify the switching of the arith global variable between True and False. The variable
    will be changed at the after exiting the function it is decorating to what ever bool is passed in.
    :param val: True or False bool that will be used to set the arith function.
    :return: return the wrapped function
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*arg: ctk.CTkEntry) -> Callable:
            global arith
            try:
                result = func(*arg)
            finally:
                arith = val
            return result
        return wrapper
    return decorator


# function do disable buttons when the result becomes Undefined.
def change_button_status(buttons: list[ctk.CTkButton]) -> None:
    """
    A function to disable certain buttons (determined by the list of buttons passed in to the function) when 'UNDEFINED'
    is displayed in current_text. In the function we refer to status_var but this StringVar object is linked to the
    Entry object during initiation of the global variable current_text.
    :param buttons: A list of Button objects to be disabled when 'UNDEFINED' is displayed in current_text.
    :return: None
    """
    if status_var.get() == "UNDEFINED":
        for button in buttons:
            button.configure(state=ctk.DISABLED)
    else:
        for button in buttons:
            button.configure(state=ctk.NORMAL)


# TODO not sure if this function is necessary because we no longer need to worry about unwanted characters being
# TODO inputted due to other refactoring.
# check to see if a string can be converted into a float
def check_if_float(num: str) -> bool:
    """
    A function to check if a string can be converted into a float.
    :param num: The string to be checked.
    :return: True if the string can be converted to a float, False if it cannot.
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


# TODO There are 7 paths for the logic to go through in number. However, some of the outcome is exactly the same.
# TODO The code can probably be refactored so that similar outcomes can be grouped together.
# add the functions to the buttons
@change_arith(False)
@temp_change_state()
def number(num: int) -> None:
    """
    A function to be called when a numeric button is clicked or pressed.  Depending on the situation the button
    behaves differently.  (1) If the previous button pressed is the equal button both calculation and current text are
    cleared and the new number is added to current text.  (2) If calculation text is empty and current text is 0 or
    undefined current text is cleared and the number is inserted.  (3) If calculation text is empty but current text is
    not 0 or UNDEFINED, then the number is added to the end of current text.  (4)  If there is anything in calculation
    text that doesn't fit any of the previous situations and current text is 0 delete current text and then insert the
    number.  (5) If the last character in calculation text is an arithmatic operator and arith is True delete current
    text and then insert number.  (6) If the last character in calculation text is an arithmatic operator but arith is
    false add the number to the end of current text.  (7) This is the option for any situation that does not match any
    of the above scenarios and adds the number to the end of current text.
    :param num: The number to be inserted into the entry object.
    :return: None
    """
    # print(f"Arithmatic function called with symbol: {num}")
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()

    # (1)
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, str(num))
        arith = False
        return

    if calc_text == "":
        # (2)
        if cur_text == "0" or cur_text == 'UNDEFINED':
            current_text.delete(0, END)
            current_text.insert(0, str(num))
        # (3)
        else:
            current_text.insert(END, str(num))
        return
    # (4)
    if cur_text == "0":
        arith = False  # inserted to fix a potential bug when deleting operators from the calculation text.
        current_text.delete(0, END)
        current_text.insert(0, str(num))
        return

    if calc_text[-1] in "+-x÷^":
        # (5)
        if arith is True:
            current_text.delete(0, END)
            current_text.insert(0, str(num))
            arith = False
        # (6)
        else:
            current_text.insert(END, str(num))
    # (7)
    else:
        current_text.insert(END, str(num))


# TODO for option (2) in the bellow code there doesnt seem to be any purpose to this option. Test and see if it can
# TODO be deleted.

# TODO these descriptions can be confusing and are essentially just describing the code.  Maybe i can change it to
# TODO explain why they hava that way. like explaining that you need to clear everything because a new calculation
# TODO needs to be done.

@change_arith(True)
@temp_change_state()
def arithmatic(symbol: str) -> None:
    """
    A function to be called when an arithmatic operator button is pressed.  The symbol is dependent ont which button was
    pressed.  Depending on the situation the button behaves differently.  (1) If the very end of calculation text is a
    numeric string add the symbol to the end of calculation text.  (2) im not sure why this one is here anymore. It
    might have been there to fix a bug that is no longer is there.  (3) If the very end of calculation text is '=' clear
    calculation text and insert current text into calculation text with the symbol inserted at the very end.  (4) If the
    very end of calculation text is an arithmatic operator but arith is false, add what is in the current text to the
    end of calculation text.  (5) If the very end of calculation text is an arithmatic operator and arith is true,
    delete the last thing in calculation text and insert the new symbol at the end.  (6) This is the option for anything
    that does not match any of the scenarios above.  Add the current text to calculation text along with the symbol at
    the end.
    :param symbol: arithmatic symbol that will be inserted into the calculation text.
    :return: None
    """
    # print(f"Arithmatic function called with symbol: {symbol}")
    global arith, calculation_text, current_text

    calc_text = calculation_text.get()
    cur_text = current_text.get()

    if cur_text[-1:] == ".":  # added to ensure that a 0 is added to make it look better
        current_text.delete(len(cur_text) - 1, END)
        cur_text = cur_text.replace('.', '')

    # (1)
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, symbol)
        arith = True
        return

    # (2)
    if calc_text == symbol:  # used to have cur_text == '0' or which might have been there to prevent some bug.
        arith = True
        return

    # (3)
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + symbol)
    elif calc_text and calc_text[-1:] in "+-x÷^":  # calc_text is checking if it is not an empty string
        # (4)
        if arith is False:
            calculation_text.insert(END, cur_text + symbol)
        # (5)
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, symbol)
    # (6)
    else:
        calculation_text.insert(END, cur_text + symbol)
    arith = True


# TODO when we add to negative numbers it looks like this -2+-3 which can be confusing. change it so that there
# TODO are parentheses surrounding the negative numbers like (-2)+(-3) this looks better.
# change the last numeric values sign.

@temp_change_state()
def plus_minus() -> None:
    """
    adds or takes out a negative symbol from the current text.
    :return: None
    """
    global calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if cur_text[:1] != '-' and check_if_float(cur_text) and float(cur_text) != 0:
        current_text.insert(0, '-')
    elif cur_text[:1] == '-':
        current_text.delete(0, 1)


# TODO fixed trailing decimal problem. but if the user explicitly types 0.0 it will remain 0.0 not sure if i want to
# TODO keep this behavior or not.
@change_arith(False)
@temp_change_state()
def decimal() -> None:
    """
    A function to add a decimal point. It makes sure that only one decimal point is there per number. When the
    calculation is reset after a calculation it automatically adds 0. to current text.
    :return: None
    """
    global arith, calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:] == '=':
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, '0.')
        arith = False
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


@change_arith(False)
@temp_change_state()
def clear() -> None:
    """
    Clears out calculation text as well as current text and finally adds a zero to current text.
    :return: None
    """
    global calculation_text, current_text
    calculation_text.delete(0,  END)
    current_text.delete(0, END)
    current_text.insert(0, "0")


@temp_change_state()
def backspace() -> None:
    """
    Deletes the last character in current text. If numbers run out the default zero is placed into current text. Can
    continue pressing backspace to delete the last character in calculation text, but only if current text is 0.
    :return: None
    """
    global calculation_text, current_text
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if len(cur_text) == 1:
        if cur_text == "0":
            calculation_text.delete(len(calc_text) - 1, END)
        else:
            current_text.delete(0, END)
            current_text.insert(0, "0")
    elif len(cur_text) == 2 and cur_text[0] == '-':
        current_text.delete(0, END)
        current_text.insert(0, '0')
    else:
        current_text.delete(len(cur_text) - 1, END)


# TODO refactor code so that a good junk of the code is under the try clause. still not sure if this is best approach
# TODO or not. originally added it just to deal with zer division errors.

# TODO Add way for the equal button to memorize the last operation and repeat that continuously
# TODO as long as the used keeps pressing the equals button.
# I was not able to build an eval() function that follows the order of operations.
# so I just used the built-in eval() function.
@change_arith(False)
@temp_change_state()
def equal() -> None:
    """
    A function that signals the calculation that the text should be evaluated and place the answer to the current text
    and then place the calculation done including an '=' at the end of the calculation text.  This also replaces common
    math operators to operators used in python. such as changing '÷' to '/'.  Handles zero division by placing
    'UNDEFINED' in current text.  Converts the answer to integer if doing so doesn't result in a different number
    (changing 1.2 -> 1 won't be possible.)
    :return: None
    """
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
    return


def key_binds(key: Event) -> None:
    """
    A function that searches the matching keypress to the matching button and invokes that function. In essence binding
    keys to specific buttons on the calculator.
    :param key: Event object that represents a key being pressed on the keyboard.
    :return: None
    """
    # print(f"Key pressed: {key.keysym}")
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


# this allows for different behaviors of each button depending on whether the last button was a numeric button
# or an arithmatic button such as "+-/*^"
arith = False  # to check if the last entry in the calculation_text is an arithmetic operator.

root = ctk.CTk()
root.bind("<Key>", key_binds)  # this binds the key_binds function to the CTk window.
set_appearance_mode("dark")

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
                         command=lambda: number(1))
button_2 = ctk.CTkButton(root, text="2", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(2))
button_3 = ctk.CTkButton(root, text="3", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(3))
button_4 = ctk.CTkButton(root, text="4", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(4))
button_5 = ctk.CTkButton(root, text="5", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(5))
button_6 = ctk.CTkButton(root, text="6", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(6))
button_7 = ctk.CTkButton(root, text="7", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(7))
button_8 = ctk.CTkButton(root, text="8", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(8))
button_9 = ctk.CTkButton(root, text="9", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(9))
button_0 = ctk.CTkButton(root, text="0", width=width, height=height, border_width=border, font=button_font,
                         command=lambda: number(0))
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
                                  command=plus_minus)
button_decimal = ctk.CTkButton(root, text=".", width=width, height=height, border_width=border, font=button_font,
                               command=decimal)
button_backspace = ctk.CTkButton(root, text="<-X", width=width, height=height, border_width=border, font=button_font,
                                 command=backspace)
button_clear = ctk.CTkButton(root, text="Clear", width=width, height=height, border_width=border, font=button_font,
                             command=clear)
button_equal = ctk.CTkButton(root, text="=", width=width * 2, height=height, border_width=border, font=button_font,
                             command=equal)


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


if __name__ == '__main__':
    root.mainloop()
