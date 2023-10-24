"""
This is a work in progress and I intend to expand it so that I can do linear algebra as well
as statistical calculations so that I can quickly verify that my data analysis is being done
correctly.

This version is the new implementation using object-oriented programing.

Currently, can only perform simple arithmatic with +-/*^
"""


# TODO change formatting for constants to all caps

# Imports
import customtkinter as ctk
from customtkinter import set_appearance_mode, END
# Callable is for when a function is returned as its return value
from typing import Callable, Union


# noinspection PyAttributeOutsideInit
class SimpleCalc:

    def __init__(self, root):
        self.root = root
        self.arith = False
        self.init_buttons()
        self.init_ui()
        self.init_calculator_text()
        self.init_current_text()

    def init_buttons(self):
        # define font and size for buttons
        self.button_font = ('Lucida Console', 20)

        # variables to adjust button size
        self.text_width = 400
        self.width = int(self.text_width // 3.75)
        self.height = 50
        self.border = 1

        # add buttons for the numbers
        self.button_1 = ctk.CTkButton(self.root, text='1', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(1))
        self.button_2 = ctk.CTkButton(self.root, text='2', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(2))
        self.button_3 = ctk.CTkButton(self.root, text='3', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(3))
        self.button_4 = ctk.CTkButton(self.root, text='4', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(4))
        self.button_5 = ctk.CTkButton(self.root, text='5', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(5))
        self.button_6 = ctk.CTkButton(self.root, text='6', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(6))
        self.button_7 = ctk.CTkButton(self.root, text='7', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(7))
        self.button_8 = ctk.CTkButton(self.root, text='8', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, conmand=lambda: self.number(8))
        self.button_9 = ctk.CTkButton(self.root, text='9', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(9))
        self.button_0 = ctk.CTkButton(self.root, text='0', width=self.width, height=self.height,
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(0))
        self.button_add = ctk.CTkButton(self.root, text='+', width=self.width, height=self.height,
                                        border_width=self.border, font=self.button_font, command=lambda: self.arithmatic('+'))
        self.button_subtract = ctk.CTkButton(self.root, text='-', width=self.width, height=self.height,
                                             border_width=self.border, font=self.button_font, command=lambda: self.arithmatic('-'))
        self.button_multiply = ctk.CTkButton(self.root, text='⨉', width=self.width, height=self.height,
                                             border_width=self.border, font=self.button_font, command=lambda: self.arithmatic('x'))
        self.button_divide = ctk.CTkButton(self.root, text='÷', width=self.width, height=self.height,
                                           border_width=self.border, font=self.button_font, command=lambda: self.arithmatic('÷'))
        self.button_exponential = ctk.CTkButton(self.root, text='^', width=self.width, height=self.height,
                                                border_width=self.border, font=self.button_font, command=lambda: self.arithmatic('^'))
        self.button_plus_minus = ctk.CTkButton(self.root, text='+/-', width=self.width, height=self.height,
                                               border_width=self.border, font=self.button_font, command=self.plus_minus)
        self.button_decimal = ctk.CTkButton(self.root, text='.', width=self.width, height=self.height,
                                            border_width=self.border, font=self.button_font, command=self.decimal)
        self.button_backspace = ctk.CTkButton(self.root, text='<-X', width=self.width, height=self.height,
                                              border_width=self.border, font=self.button_font, command=self.backspace)
        self.button_clear = ctk.CTkButton(self.root, text='Clear', width=self.width, height=self.height,
                                          border_width=self.border, font=self.button_font, command=self.clear)
        self.button_equal = ctk.CTkButton(self.root, text='=', width=self.width * 2, height=self.height,
                                          border_width=self.border, font=self.button_font, command=self.equal)

        # TODO complete creating the different categories.
        # organize buttons into different categories.
        self.operators = [self.button_add, self.button_subtract, self.button_multiply, self.button_divide, self.button_exponential,
                     self.button_decimal, self.button_plus_minus, self.button_backspace]

    def init_ui(self):
        set_appearance_mode('dark')
        self.root.title('Simple Calculator')
        self.root.geometry('500x700')
        self.root.configure(bg='lightblue')
        self.root.resizable(True, True)  # Controls whether user can resize window.

        # get the background color of the root object
        self.root_bg_color = self.root.cget('bg')

        # put the buttons on the screen
        self.button_1.grid(row=5, column=0)
        self.button_2.grid(row=5, column=1)
        self.button_3.grid(row=5, column=2)
        self.button_4.grid(row=4, column=0)
        self.button_5.grid(row=4, column=1)
        self.button_6.grid(row=4, column=2)
        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_0.grid(row=6, column=1)
        self.button_add.grid(row=6, column=3)
        self.button_subtract.grid(row=5, column=3)
        self.button_multiply.grid(row=4, column=3)
        self.button_divide.grid(row=3, column=3)
        self.button_exponential.grid(row=8, column=0)
        self.button_plus_minus.grid(row=6, column=0)
        self.button_decimal.grid(row=6, column=2)
        self.button_clear.grid(row=7, column=1)
        self.button_backspace.grid(row=7, column=0)
        self.button_equal.grid(row=7, column=2, columnspan=2)

    def init_calculator_text(self):
        # add the text box for the numbers
        self.calculation_text = ctk.CTkEntry(root, width=self.text_width, fg_color=self.root_bg_color,
                                        border_color=self.root_bg_color, justify='right')
        self.calculation_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.calculation_text.configure(font=('Lucida Console', 15), state='readonly')
        self.calculation_text.bind('<Key>', lambda x: 'break')

    def init_current_text(self):
        # Define a string variable that will be used to keep track if undefined is displayed on current_text or not
        # in order to disable certain buttons.
        self.status_var = ctk.StringVar()
        self.status_var.trace_add('write',
                             lambda *args: self.change_button_status(self.operators))  # not sure why *args makes this work

        # add text box for current value
        self.current_text = ctk.CTkEntry(root, width=self.text_width, textvariable=self.status_var,
                                         fg_color=self.root_bg_color, border_color=self.root_bg_color, justify='right')
        self.current_text.insert(0, '0')
        self.current_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.current_text.configure(font=('Lucida Console', 30), state='readonly')

    # Decorator function to change the state of entry objects.
    def temp_change_state(self) -> Callable:
        """
        A decorator function that will be applied to most of the functions relating to button inputs.  The Entry objects
        are set up in a way that they are readonly and the user can not type into them directly.  Only when a button is
        pressed can the entry object texts change.  When ever a function with this decorator is invoked it enables the entry
        objects to normal, the functions then change the text through the operations, then finally it changes the state back
        to read only.  Global variables are being used to avoid invocation during evaluation by the interpreter because I
        want to  keep these variables close to the entry UI elements of the script for organization.
        :return: return the wrapped function.
        """
        def decorator(func: Callable) -> Callable:
            def wrapper(*arg: ctk.CTkEntry) -> Callable:
                self.calculation_text.configure(state='normal')
                self.current_text.configure(state='normal')
                try:
                    result = func(*arg)
                finally:
                    self.calculation_text.configure(state='readonly')
                    self.current_text.configure(state='readonly')
                return result
            return wrapper
        return decorator

    # decorator function to set the global variable of arith
    def change_arith(self, val: bool) -> Callable:
        """
        A decorator function to simplify the switching of the arith global variable between True and False. The variable
        will be changed at the after exiting the function it is decorating to what ever bool is passed in.
        :param val: True or False bool that will be used to set the arith function.
        :return: return the wrapped function
        """
        def decorator(func: Callable) -> Callable:
            def wrapper(*arg: ctk.CTkEntry) -> Callable:
                try:
                    result = func(*arg)
                finally:
                    self.arith = val
                return result
            return wrapper
        return decorator

    # function do disable buttons when the result becomes Undefined.
    def change_button_status(self, buttons: list[ctk.CTkButton]) -> None:
        """
        A function to disable certain buttons (determined by the list of buttons passed in to the function) when 'UNDEFINED'
        is displayed in current_text. In the function we refer to status_var but this StringVar object is linked to the
        Entry object during initiation of the global variable current_text.
        :param buttons: A list of Button objects to be disabled when 'UNDEFINED' is displayed in current_text.
        :return: None
        """
        if self.status_var.get() == 'UNDEFINED':
            for button in buttons:
                button.configure(state=ctk.DISABLED)
        else:
            for button in buttons:
                button.configure(state=ctk.NORMAL)

    # TODO not sure if this function is necessary because we no longer need to worry about unwanted characters being
    # TODO inputted due to other refactoring.
    # check to see if a string can be converted into a float
    @staticmethod
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


if __name__ == '__main__':
    root = ctk.CTk()
    calc = SimpleCalc(root)
    root.mainloop()