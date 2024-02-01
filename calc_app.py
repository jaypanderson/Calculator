"""
This will be the main script to run the calculator app.  All the different calculators will be organized in to their own
module and class and will be imported here so that it can be run.  The default calculator will be simple calculator.
"""
import tkinter as tk
import customtkinter as ctk
from simple_calculator import SimpleCalc
from matrix_calculator import MatrixCalc


class MainApp:

    def __init__(self, root):
        self.root = root
        self.current_calculator_frame = None
        self.root_bg_color = self.root.cget('bg')
        #print(self.root_bg_color)

        menu_frame = ctk.CTkFrame(self.root, border_color='gray92')
        menu_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.calculator_options = {'Simple': SimpleCalc,
                                   'Matrix': MatrixCalc}

        self.calculator_var = ctk.StringVar(self.root)
        self.calculator_var.set('Simple')
        self.option_menu = ctk.CTkOptionMenu(menu_frame, width=150, values=list(self.calculator_options.keys()), command=self.switch_calculator)
        self.option_menu.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.switch_calculator('Simple')

    def switch_calculator(self, selection):
        if self.current_calculator_frame:
            self.current_calculator_frame.destroy()

        calculator_class = self.calculator_options[selection]
        self.current_calculator_frame = calculator_class(self.root)
        #self.option_menu.grid(row=0, column=0, columnspan=4, sticky="ew")


if __name__ == '__main__':
    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()
