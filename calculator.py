"""
This is a work in progress and I intend to expand it so that I can do linear algebra as well
as statistical calculations so that I can quickly verify that my data analysis is being done
correctly.

This version is the new implementation using object-oriented programing.

Currently, can only perform simple arithmatic with +-/*^
"""


# Imports
import customtkinter as ctk
from customtkinter import set_appearance_mode, END
# Callable is for when a function is returned as its return value
from typing import Callable, Union

class SimpleCalc:

    def __init__(self, root):
        self.root = root
        self.arith = False
        self.init_calculator_text()
        self.init_current_text()
        self.init_buttons()
        self.init_ui()

    def init_calculator_text(self):
        pass

    def init_current_text(self):
        pass

    def \
            init_self(self):
        # define font and size for buttons
        self.button_font = ('Lucida Console', 20)

        # variables to adjust button size
        self.text_width = 400
        self.width = int(self.text_width // 3.75)
        self.height = 50
        self.border = 1

        # add buttons for the numbers
        button_1 = ctk.CTkButton(root, text='1', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(1))
        button_2 = ctk.CTkButton(root, text='2', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(2))
        button_3 = ctk.CTkButton(root, text='3', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(3))
        button_4 = ctk.CTkButton(root, text='4', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(4))
        button_5 = ctk.CTkButton(root, text='5', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(5))
        button_6 = ctk.CTkButton(root, text='6', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(6))
        button_7 = ctk.CTkButton(root, text='7', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(7))
        button_8 = ctk.CTkButton(root, text='8', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, conmand=lambda: self.number(8))
        button_9 = ctk.CTkButton(root, text='9', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(9))
        button_0 = ctk.CTkButton(root, text='0', width=self.width, height=self.height, border_width=self.border,
                                 font=self.button_font, command=lambda: self.number(0))
        button_add = ctk.CTkButton(root, text='+', width=self.width, height=self.height, border_width=self.border,
                                   font=self.button_font, command=lambda: self.arithmatic('+'))
        button_subtract = ctk.CTkButton(root, text='-', width=self.width, height=self.height, border_width=self.border,
                                        font=self.button_font, command=lambda: self.arithmatic('-'))
        button_multiply = ctk.CTkButton(root, text='⨉', width=self.width, height=self.height, border_width=self.border,
                                        font=self.button_font, command=lambda: self.arithmatic('x'))
        button_divide = ctk.CTkButton(root, text='÷', width=self.width, height=self.height, border_width=self.border,
                                      font=self.button_font, command=lambda: self.arithmatic('÷'))
        button_exponential = ctk.CTkButton(root, text='^', width=self.width, height=self.height, border_width=self.border,
                                           font=self.button_font, command=lambda: self.arithmatic('^'))
        button_plus_minus = ctk.CTkButton(root, text='+/-', width=self.width, height=self.height, border_width=self.border,
                                          font=self.button_font, command=self.plus_minus)
        button_decimal = ctk.CTkButton(root, text='.', width=self.width, height=self.height, border_width=self.border,
                                       font=self.button_font, command=self.decimal)
        button_backspace = ctk.CTkButton(root, text='<-X', width=self.width, height=self.height, border_width=self.border,
                                         font=self.button_font, command=self.backspace)
        button_clear = ctk.CTkButton(root, text='Clear', width=self.width, height=self.height, border_width=self.border,
                                     font=self.button_font, command=self.clear)
        button_equal = ctk.CTkButton(root, text='=', width=self.width * 2, height=self.height, border_width=self.border,
                                     font=self.button_font, command=self.equal)

    def init_ui(self):
        set_appearance_mode('dark')
        self.root.title('Simple Calculator')
        self.root.geometry('500x700')
        self.root.configure(bg='lightblue')
        self.root.resizable(True, True)  # Controls whether user can resize window.
        pass




if __name__ == '__main__':
     root = ctk.CTk()
     calc = SimpleCalc(root)
     root.mainloop()