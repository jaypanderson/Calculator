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
    def test_self_1(self):
        button_click(1)
        self.assert_state(False, '', '1')
        button_click(3)
        self.assert_state(False, '', '13')

    def test_self_2(self):
        arithmatic('+')
        self.assert_state(True, '0+', '0')
        self.assertEqual(current_text.get(), '0')
        self.assertEqual(calculation_text.get(), '0+')

    # Test number and arithmatic button together.
    def test_num_arith_1(self):
        button_click(1)
        arithmatic('+')
        self.assertEqual(current_text.get(), '1')
        self.assertEqual(calculation_text.get(), '1+')

    def test_num_arith_2(self):
        arithmatic('+')
        button_click(1)
        self.assertEqual(current_text.get(), '1')
        self.assertEqual(calculation_text.get(), '0+')

    def test_num_arith_3(self):
        button_click(2)
        arithmatic('+')
        button_click(3)
        self.assertEqual(current_text.get(), '3')
        self.assertEqual(calculation_text.get(), '2+')


if __name__ == '__main__':
    unittest.main()
