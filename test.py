import unittest
import calculator as calc
from calculator import *


# Because arith is an immutable bool value we need to use calc.arith so that the arith variable in the calculation
# module is
class MyTestCase(unittest.TestCase):
    @ temp_change_state()
    def setUp(self) -> None:
        calc.arith = False
        calc.calculation_text.delete(0, END)
        calc.current_text.delete(0, END)
        calc.current_text.insert(0, '0')

    # helper function to compact assertions in tests.
    def assert_state(self, exp_arith, exp_calc_text, exp_cur_text) -> None:
        self.assertEqual(exp_arith, calc.arith)
        self.assertEqual(exp_calc_text, calc.calculation_text.get())
        self.assertEqual(exp_cur_text, calc.current_text.get())

    # Test buttons by themselves
    def test_num(self):
        number(0)
        self.assert_state(False, '', '0')
        number(0)
        self.assert_state(False, '', '0')
        number(1)
        self.assert_state(False, '', '1')
        number(0)
        self.assert_state(False, '', '10')
        number(3)
        self.assert_state(False, '', '103')

    def test_arith(self):
        arithmatic('+')
        self.assert_state(True, '0+', '0')
        arithmatic('+')
        self.assert_state(True, '0+', '0')
        arithmatic('x')
        self.assert_state(True, '0x', '0')
        arithmatic('÷')
        self.assert_state(True, '0÷', '0')
        arithmatic('-')
        self.assert_state(True, '0-', '0')

    def test_plus_minus(self):
        plus_minus()
        self.assert_state(False, '', '0')
        plus_minus()
        self.assert_state(False, '', '0')

    def test_decimal(self):
        decimal()
        self.assert_state(False, '', '0.')
        decimal()
        self.assert_state(False, '', '0')

    def test_clear(self):
        clear()
        self.assert_state(False, '', '0')
        clear()
        self.assert_state(False, '', '0')

    def test_backspace(self):
        backspace()
        self.assert_state(False, '', '0')
        backspace()
        self.assert_state(False, '', '0')

    def test_equal(self):
        equal()
        self.assert_state(False, '0=', '0')
        equal()
        self.assert_state(False, '0=', '0')

    # Test number and arithmatic button together.
    def test_num_arith_1(self):
        number(1)
        self.assert_state(False, '', '1')
        arithmatic('+')
        self.assert_state(True, '1+', '1')
        number(9)
        self.assert_state(False, '1+', '9')
        arithmatic('x')
        self.assert_state(True, '1+9x', '9')

    def test_num_arith_2(self):
        arithmatic('+')
        self.assert_state(True, '0+', '0')
        number(1)
        self.assert_state(False, '0+', '1')
        number(9)
        self.assert_state(False, '0+', '19')
        arithmatic('÷')
        self.assert_state(True, '0+19÷', '19')
        arithmatic('x')
        self.assert_state(True, '0+19x', '19')
        arithmatic('-')
        self.assert_state(True, '0+19-', '19')
        number(3)
        self.assert_state(False, '0+19-', '3')
        number(3)
        self.assert_state(False, '0+19-', '33')

    def test_num_dec_1(self):
        number(7)
        self.assert_state(False, '', '7')
        decimal()
        self.assert_state(False, '', '7.')
        decimal()
        self.assert_state(False, '', '7')
        number(4)
        self.assert_state(False, '', '74')
        decimal()
        self.assert_state(False, '', '74.')
        number(9)
        self.assert_state(False, '', '74.9')
        decimal()
        self.assert_state(False, '', '74.9')

    def test_num_plus_minus_1(self):
        number(4)
        self.assert_state(False, '', '4')
        plus_minus()
        self.assert_state(False, '', '-4')
        plus_minus()
        self.assert_state(False, '', '4')
        plus_minus()
        self.assert_state(False, '', '-4')
        number(7)
        self.assert_state(False, '', '-47')
        number(3)
        self.assert_state(False, '', '-473')
        plus_minus()
        self.assert_state(False, '', '473')
        plus_minus()
        self.assert_state(False, '', '-473')

    def test_arith_dec_1(self):
        arithmatic('x')
        self.assert_state(True, '0x', '0')
        decimal()
        self.assert_state(False, '0x', '0.')











    # TODO this bug can probably be fixed by creating a wrapper function that changes the arith global variable
    def test_found_bugs_1(self):
        # this involves the functions number, decimal, arithmatic and equal. The bug would appear the situation as
        # appears bellow and would delete the number and just insert 0, instead of adding a decimal to the previous
        # number.  The bug was fixed by making sure arith changes to false when ever decimal
        number(6)
        self.assert_state(False, '', '6')
        arithmatic('x')
        self.assert_state(True, '6x', '6')
        equal()
        self.assert_state(True, '6x6=', '36')
        number(8)
        self.assert_state(True, '', '8')
        decimal()
        self.assert_state(False, '', '8.') # used to appear as (True, '', '0.')



if __name__ == '__main__':
    unittest.main()
