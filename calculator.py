"""
This is a work in progress and I intend to expand it so that I can do linear algebra as well
as statistical calculations so that I can quickly verify that my data analysis is being done
correctly.

This version is the new implementation using object-oriented programing.

Currently, can only perform simple arithmatic with +-/*^
"""
# using tkinter for now because i cant find its equivalent in customtkinter.
from tkinter import Event


# Imports
import customtkinter as ctk
from customtkinter import set_appearance_mode, END
# Callable is for when a function is returned as its return value
from typing import Callable, Union

# TODO change formatting for constants to all caps

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
                                      border_width=self.border, font=self.button_font, command=lambda: self.number(8))
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
        self.status_var.trace_add('write', lambda *args: self.change_button_status(self.operators))  # not sure why *args makes this work

        # add text box for current value
        self.current_text = ctk.CTkEntry(root, width=self.text_width, textvariable=self.status_var,
                                         fg_color=self.root_bg_color, border_color=self.root_bg_color, justify='right')
        self.current_text.insert(0, '0')
        self.current_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.current_text.configure(font=('Lucida Console', 30), state='readonly')



    class Decorators:
        # Decorator function to change the state of entry objects.
        @staticmethod
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
            def decorator(func: Callable) -> Callable:
                def wrapper(self, *arg: ctk.CTkEntry) -> Callable:
                    self.calculation_text.configure(state='normal')
                    self.current_text.configure(state='normal')
                    try:
                        result = func(self, *arg)
                    finally:
                        self.calculation_text.configure(state='readonly')
                        self.current_text.configure(state='readonly')
                    return result
                return wrapper
            return decorator

        # decorator function to set the global variable of arith
        # it is set as static method, but its not actually a static method. it is responsible
        @staticmethod
        def change_arith(val: bool) -> Callable:
            """
            A decorator function to simplify the switching of the arith global variable between True and False. The variable
            will be changed at the after exiting the function it is decorating to what ever bool is passed in.
            :param val: True or False bool that will be used to set the arith function.
            :return: return the wrapped function
            """
            def decorator(func: Callable) -> Callable:
                def wrapper(self, *arg: ctk.CTkEntry) -> Callable:
                    try:
                        result = func(self, *arg)
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

    # TODO There are 7 paths for the logic to go through in number. However, some of the outcome is exactly the same.
    # TODO The code can probably be refactored so that similar outcomes can be grouped together.
    # add the functions to the buttons
    @Decorators.change_arith(False)
    @Decorators.temp_change_state()
    def number(self, num: int) -> None:
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
        # print(f'Arithmatic function called with symbol: {num}')
        calc_text = self.calculation_text.get()
        cur_text = self.current_text.get()

        # (1)
        if calc_text[-1:] == '=':
            self.calculation_text.delete(0, END)
            self.current_text.delete(0, END)
            self.current_text.insert(0, str(num))
            return

        if calc_text == '':
            # (2)
            if cur_text == '0' or cur_text == 'UNDEFINED':
                self.current_text.delete(0, END)
                self.current_text.insert(0, str(num))
            # (3)
            else:
                self.current_text.insert(END, str(num))
            return
        # (4)
        if cur_text == '0':
            self.current_text.delete(0, END)
            self.current_text.insert(0, str(num))
            return

        if calc_text[-1] in '+-x÷^':
            # (5)
            if self.arith is True:
                self.current_text.delete(0, END)
                self.current_text.insert(0, str(num))
            # (6)
            else:
                self.current_text.insert(END, str(num))
        # (7)
        else:
            self.current_text.insert(END, str(num))

    # TODO for option (2) in the bellow code there doesnt seem to be any purpose to this option. Test and see if it can
    # TODO be deleted.

    # TODO these descriptions can be confusing and are essentially just describing the code.  Maybe i can change it to
    # TODO explain why they hava that way. like explaining that you need to clear everything because a new calculation
    # TODO needs to be done.

    @Decorators.change_arith(True)
    @Decorators.temp_change_state()
    def arithmatic(self, symbol: str) -> None:
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
        # print(f'Arithmatic function called with symbol: {symbol}')

        calc_text = self.calculation_text.get()
        cur_text = self.current_text.get()

        if cur_text[-1:] == '.':  # added to ensure that a 0 is added to make it look better
            self.current_text.delete(len(cur_text) - 1, END)
            cur_text = cur_text.replace('.', '')

        if cur_text == '-0':  # bug fix
            self.current_text.delete(0)
            cur_text = cur_text[1:]

        # (1)
        if calc_text[-1:].isnumeric():
            self.calculation_text.insert(END, symbol)
            return

        # (2)
        if calc_text == symbol:  # used to have cur_text == '0' or which might have been there to prevent some bug.
            return

        # (3)
        if calc_text[-1:] == '=':
            self.calculation_text.delete(0, END)
            self.calculation_text.insert(0, cur_text + symbol)
        elif calc_text and calc_text[-1:] in '+-x÷^':  # calc_text is checking if it is not an empty string
            # (4)
            if self.arith is False:
                self.calculation_text.insert(END, cur_text + symbol)
            # (5)
            else:
                self.calculation_text.delete(len(calc_text) - 1, END)
                self.calculation_text.insert(END, symbol)
        # (6)
        else:
            self.calculation_text.insert(END, cur_text + symbol)

    # TODO when we add to negative numbers it looks like this -2+-3 which can be confusing. change it so that there
    # TODO are parentheses surrounding the negative numbers like (-2)+(-3) this looks better.
    # change the last numeric values sign.

    @Decorators.temp_change_state()
    def plus_minus(self) -> None:
        """
        adds or takes out a negative symbol from the current text.
        :return: None
        """

        calc_text = self.calculation_text.get()
        cur_text = self.current_text.get()
        if cur_text[:1] != '-' and self.check_if_float(cur_text) and float(cur_text) != 0:
            self.current_text.insert(0, '-')
        elif cur_text[:1] == '-':
            self.current_text.delete(0, 1)

    # TODO fixed trailing decimal problem. but if the user explicitly types 0.0 it will remain 0.0 not sure if i want to
    # TODO keep this behavior or not.
    @Decorators.change_arith(False)
    @Decorators.temp_change_state()
    def decimal(self) -> None:
        """
        A function to add a decimal point. It makes sure that only one decimal point is there per number. When the
        calculation is reset after a calculation it automatically adds 0. to current text.
        :return: None
        """

        calc_text = self.calculation_text.get()
        cur_text = self.current_text.get()
        if calc_text[-1:] == '=':
            self.calculation_text.delete(0, END)
            self.current_text.delete(0, END)
            self.current_text.insert(0, '0.')
            return

        if self.arith is True:
            self.current_text.delete(0, END)
            self.current_text.insert(0, '0.')
        else:
            if '.' not in cur_text:
                self.current_text.insert(END, '.')
            elif '.' in cur_text and cur_text[-1] == '.':
                self.current_text.delete(len(cur_text) - 1, END)

    @Decorators.change_arith(False)
    @Decorators.temp_change_state()
    def clear(self) -> None:
        """
        Clears out calculation text as well as current text and finally adds a zero to current text.
        :return: None
        """

        self.calculation_text.delete(0, END)
        self.current_text.delete(0, END)
        self.current_text.insert(0, '0')

    # helper function to find the last occurrence of an arithmatic operator symbol
    @staticmethod
    def find_last_arith(calc: str) -> Union[int, None]:
        """
        A function to find out the location of the second to last operator in a string so that the backspace function knows
        where to delete. This allows for chunks of the text to be deleted instead of one by one.
        ex) '36x54+32=' -> '36x54'+ -> '36x' -> ''
        :param calc: A string that represents the calculation_text. ex) 36x54+32=
        :return: This will return the second occurrence of an operator including the equal symbol.  If there is no operator
        or if there is only one operator None will be returned.
        """
        symbols = 'x÷+-^='
        last = None
        second_last = None
        for i, val in enumerate(calc):
            if val in symbols:
                second_last = last
                last = i
        return second_last

    @Decorators.temp_change_state()
    def backspace(self) -> None:
        """
        Deletes the last character in current text. If numbers run out the default zero is placed into current text. Can
        continue pressing backspace to delete the last character in calculation text, but only if current text is 0.
        :return: None
        """

        calc_text = self.calculation_text.get()
        cur_text = self.current_text.get()
        if len(cur_text) == 1:
            if cur_text == '0':
                index = self.find_last_arith(calc_text)
                if index is None:
                    self.calculation_text.delete(0, END)
                else:
                    self.calculation_text.delete(index + 1, END)
            else:
                self.current_text.delete(0, END)
                self.current_text.insert(0, '0')
        elif len(cur_text) == 2 and cur_text[0] == '-':
            self.current_text.delete(0, END)
            self.current_text.insert(0, '0')
        else:
            self.current_text.delete(len(cur_text) - 1, END)

    # TODO refactor code so that a good junk of the code is under the try clause. still not sure if this is best approach
    # TODO or not. originally added it just to deal with zer division errors.

    # TODO Add way for the equal button to memorize the last operation and repeat that continuously
    # TODO as long as the used keeps pressing the equals button.
    # I was not able to build an eval() function that follows the order of operations.
    # so I just used the built-in eval() function.
    @Decorators.change_arith(False)
    @Decorators.temp_change_state()
    def equal(self) -> None:
        """
        A function that signals the calculation that the text should be evaluated and place the answer to the current text
        and then place the calculation done including an '=' at the end of the calculation text.  This also replaces common
        math operators to operators used in python. such as changing '÷' to '/'.  Handles zero division by placing
        'UNDEFINED' in current text.  Converts the answer to integer if doing so doesn't result in a different number
        (changing 1.2 -> 1 won't be possible.)
        :return: None
        """
        calc_text = self.calculation_text.get()
        calc_text = calc_text.replace('x', '*')
        calc_text = calc_text.replace('÷', '/')
        calc_text = calc_text.replace('^', '**')  # change the ^ to ** because in python ^ is bitwise XOR operator.
        cur_text = self.current_text.get()

        if cur_text[-1] == '.':  # added to ensure that trailing decimal points are removed from numbers.
            cur_text = cur_text[:-1]

        if calc_text[-1:] == '=':
            return

        try:
            eval(calc_text + cur_text)
        except ZeroDivisionError:
            self.calculation_text.delete(0, END)
            self.current_text.delete(0, END)
            self.current_text.insert(0, 'UNDEFINED')
            return

        ans = eval(calc_text + cur_text)
        if ans == int(ans):
            ans = int(ans)
        self.current_text.delete(0, END)
        self.current_text.insert(0, str(round(ans, ndigits=14)))
        self.calculation_text.insert(END, cur_text + '=')
        return

    def key_binds(self, key: Event) -> None:
        """
        A function that searches the matching keypress to the matching button and invokes that function. In essence binding
        keys to specific buttons on the calculator.
        :param key: Event object that represents a key being pressed on the keyboard.
        :return: None
        """
        # print(f'Key pressed: {key.keysym}')
        key_map = {'1': self.button_1,
                   '2': self.button_2,
                   '3': self.button_3,
                   '4': self.button_4,
                   '5': self.button_5,
                   '6': self.button_6,
                   '7': self.button_7,
                   '8': self.button_8,
                   '9': self.button_9,
                   '0': self.button_0,
                   '+': self.button_add,
                   '-': self.button_subtract,
                   '*': self.button_multiply,
                   '/': self.button_divide,
                   '^': self.button_exponential,
                   '.': self.button_decimal}

        special_keys = {'BackSpace': self.button_backspace,
                        'Return': self.button_equal,
                        'Escape': self.button_clear}
        if key.char in key_map:
            func = key_map.get(key.char, None)
            func.invoke()
        elif key.keysym in special_keys:
            func = special_keys.get(key.keysym, None)
            func.invoke()


if __name__ == '__main__':
    root = ctk.CTk()
    calc = SimpleCalc(root)
    root.mainloop()