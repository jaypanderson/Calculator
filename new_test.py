import unittest
from calculator import SimpleCalc
import customtkinter as ctk



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # tc is short for test calc
        self.root = ctk.CTk()
        self.tc = SimpleCalc(self.root)
    def assert_state(self, exp_arith, exp_calc_text, exp_cur_text) -> None:
        self.assertEqual(exp_arith, self.tc.arith)
        self.assertEqual(exp_calc_text, self.tc.calculation_text.get())
        self.assertEqual(exp_cur_text, self.tc.current_text.get())

    def test_num(self):
        self.tc.number(0)
        self.assert_state(False, '', '0')
        self.tc.number(0)
        self.assert_state(False, '', '0')
        self.tc.number(1)
        self.assert_state(False, '', '1')
        self.tc.number(0)
        self.assert_state(False, '', '10')
        self.tc.number(3)
        self.assert_state(False, '', '103')

    def test_arith(self):
        self.tc.arithmatic('+')
        self.assert_state(True, '0+', '0')
        self.tc.arithmatic('+')
        self.assert_state(True, '0+', '0')
        self.tc.arithmatic('x')
        self.assert_state(True, '0x', '0')
        self.tc.arithmatic('÷')
        self.assert_state(True, '0÷', '0')
        self.tc.arithmatic('-')
        self.assert_state(True, '0-', '0')

    def test_plusminus(self):
        self.tc.plus_minus()
        self.assert_state(False, '', '0')
        self.tc.plus_minus()
        self.assert_state(False, '', '0')

    def test_decimal(self):
        self.tc.decimal()
        self.assert_state(False, '', '0.')
        self.tc.decimal()
        self.assert_state(False, '', '0')

    def test_clear(self):
        self.tc.clear()
        self.assert_state(False, '', '0')
        self.tc.clear()
        self.assert_state(False, '', '0')

    def test_backspace(self):
        self.tc.backspace()
        self.assert_state(False, '', '0')
        self.tc.backspace()
        self.assert_state(False, '', '0')

    def test_equal(self):
        self.tc.equal()
        self.assert_state(False, '0=', '0')
        self.tc.equal()
        self.assert_state(False, '0=', '0')

    # Test number and arithmatic button together.
    def test_num_arith_1(self):
        self.tc.number(1)
        self.assert_state(False, '', '1')
        self.tc.arithmatic('+')
        self.assert_state(True, '1+', '1')
        self.tc.number(9)
        self.assert_state(False, '1+', '9')
        self.tc.arithmatic('x')
        self.assert_state(True, '1+9x', '9')

if __name__ == '__main__':
    unittest.main()


