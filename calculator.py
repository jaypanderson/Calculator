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
        self.init_calculator_text(self)
        self.init_current_text(self)
        self.init_buttons()

    def init_calculator_text(self):
        pass

    def init_current_text(self):
        pass

    def init_buttons(self):
        pass




if __name__ == '__main__':
    pass