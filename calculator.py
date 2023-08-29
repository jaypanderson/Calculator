# I want to build a calculator app.

# use tkinter to create a GUI

from tkinter import *
from tkinter import END
import math


# add the functions to the buttons
def button_click(number):
    global arith
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
        arith = False # inserted to fix a potential bug when deleting operators from the calculation text.
        current_text.delete(0, END)
        current_text.insert(0, str(number))
        return
    if calc_text[-1] in  "+-*/^":
        if arith ==True:
            current_text.delete(0, END)
            current_text.insert(0, str(number))
            arith = False
        else:
            current_text.insert(END, str(number))
        return
    else:
        current_text.insert(END, str(number))


def button_add():
    global arith

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, "+")
        arith = True
        return
    if cur_text == "0" or calc_text == "+":
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + "+")
    elif calc_text and calc_text[-1:] in "+-*/^": # calc_text is checking so it is not an empty string
        if arith == False:
            calculation_text.insert(END, current_text.get() + "+")
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, "+")
    else:
        calculation_text.insert(END, current_text.get() + "+")
    arith = True


def button_subtract():
    global arith

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, "-")
        arith = True
        return
    if cur_text == "0" or calc_text == "-":
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + "-")
    elif calc_text and calc_text[-1:] in "+-*/^": # calc_text is checking so it is not an empty string
        if arith == False:
            calculation_text.insert(END, current_text.get() + "-")
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, "-")
    else:
        calculation_text.insert(END, current_text.get() + "-")
    arith = True


def button_multiply():
    global arith

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, "*")
        arith = True
        return
    if cur_text == "0" or calc_text == "*":
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + "*")
    elif calc_text and calc_text[-1:] in "+-*/^": # calc_text is checking so it is not an empty string
        if  arith == False:
            calculation_text.insert(END, current_text.get() + "*")
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, "*")
    else:
        calculation_text.insert(END, current_text.get() + "*")
    arith = True


def button_divide():
    global arith

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, "/")
        arith = True
        return
    if cur_text == "0" or calc_text == "/":
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + "/")
    elif calc_text and calc_text[-1:] in "+-*/^": # calc_text is checking so it is not an empty string
        if arith == False:
            calculation_text.insert(END, current_text.get() + "/")
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, "/")
    else:
        calculation_text.insert(END, current_text.get() + "/")
    arith = True


def button_exponential():
    global arith

    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if calc_text[-1:].isnumeric():
        calculation_text.insert(END, "^")
        arith = True
        return
    if cur_text == "0" or calc_text == "^":
        arith = True
        return
    if calc_text[-1:] == "=":
        calculation_text.delete(0, END)
        calculation_text.insert(0, cur_text + "^")
    elif calc_text and calc_text[-1:] in "+-*/^": # calc_text is checking so it is not an empty string
        if  arith == False:
            calculation_text.insert(END, current_text.get() + "^")
        else:
            calculation_text.delete(len(calc_text)-1, END)
            calculation_text.insert(END, "^")
    else:
        calculation_text.insert(END, current_text.get() + "^")
    arith = True


# change the last numeric values sign.
def button_plus_minus():
    pass


def button_decimal():
    pass


def button_clear():
    calculation_text.delete(0,  END)
    current_text.delete(0, END)
    current_text.insert(0, "0")


def button_backspace():
    calc_text = calculation_text.get()
    cur_text = current_text.get()
    if len(cur_text) == 1:
        if  cur_text == "0":
            calculation_text.delete(len(calc_text) - 1, END)
        else:
            current_text.delete(0, END)
            current_text.insert(0, "0")
    else:
        current_text.delete(len(cur_text) - 1, END)


# i was not able to build a an eval() function that follows the order of operationss.
# so i just used the built in eval() function.
def button_equal():
    calc_text = calculation_text.get()
    calc_text = calc_text.replace("^", "**") # change the ^ to ** because in python ^ is bitwize XOR operator.
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


root = Tk()
# this allows for different behaviors of each button depending on wether the last button was a numeric button
# or an arithmatic button such as "+-/*"
arith = False # to check if the last entry in the calculation_text is an arithmetic operator.

root.title("Simple Calculator")
root.geometry("500x700")
root.configure(bg="lightblue")
root.resizable(0, 0)


# add the text box for the numbers
calculation_text = Entry(root, width=58, borderwidth=5)
calculation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# add text box for current value
current_text = Entry(root, width=16, borderwidth=5)
current_text.insert(0, "0")
current_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
current_text.configure(font=("Arial", 30))


# define button font and size
button_font = ("Arial", 30)


# add buttons for the numbers
button_1 = Button(root, text="1", padx=25, pady=5, font=button_font, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=25, pady=5, font=button_font, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=25, pady=5, font=button_font, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=25, pady=5, font=button_font, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=25, pady=5, font=button_font, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=25, pady=5, font=button_font, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=25, pady=5, font=button_font, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=25, pady=5, font=button_font, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=25, pady=5, font=button_font, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=25, pady=5, font=button_font, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=14, pady=5, font=button_font, command=button_add)
button_subtract = Button(root, text="-", padx=19, pady=5, font=button_font, command=button_subtract)
button_multiply = Button(root, text="⨉", padx=10, pady=5, font=button_font, command=button_multiply)
button_divide = Button(root, text="÷", padx=8, pady=4, font=("UD Digi Kyokasho N-R", 30), command=button_divide)
button_exponential = Button(root, text="^", padx=26, pady=5, font=button_font, command=button_exponential)
button_plus_minus = Button(root, text="+/-", padx=13, pady=5, font=button_font, command=button_plus_minus)
button_decimal = Button(root, text=".", padx=30, pady=5, font=button_font, command=button_decimal)
button_backspace =  Button(root, text="<-X", padx=21, pady=5, font=("Arial", 20), command=button_backspace)
button_clear = Button(root, text="Clear", padx=9, pady=5, font=("Arial", 20), command=button_clear)
button_equal = Button(root, text="=", padx=72, pady=1, font=("Arial", 24), command=button_equal)

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
