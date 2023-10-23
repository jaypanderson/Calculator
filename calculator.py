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

    def init_buttons(self):
        # define font and size for buttons
        self.button_font = ('Lucida Console', 20)

        # variables to adjust button size
        self.text_width = 400
        self.width = int(self.text_width // 3.75)
        self.height = 50
        self.border = 1

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