"""
This will be the main script to run the calculator app.  All the different calculators will be organized in to their own
module and class and will be imported here so that it can be run.  The default calculator will be simple calculator.
"""

import customtkinter as ctk
from simple_calculator import SimpleCalc
from matrix_calculator import MatrixCalc


class MainApp:

    def __init__(self, root):
        self.root = root
        self.calculator_options = {'Simple': SimpleCalc,
                                   'Matrix': MatrixCalc}
        self.calculator_var = ctk.StringVar(self.root)
        self.calculator_var.set('Simple')
        self.option_menu = ctk.CTkOptionMenu(root, self.calculator_var, *self.calculator_options.keys(), command=self.switch_calculator)
        self.option_menu.pack()
        self.switch_calculator('Simple')
        pass
