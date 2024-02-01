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
        self.calculator_options = {'simple': SimpleCalc,
                                   'matrix': MatrixCalc}
        self.calculator_var = ctk.StringVar()
        pass
