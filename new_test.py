import unittest
from calculator import SimpleCalc as SC



class MyTestCase(unittest.TestCase):

    def __init__(self):
        # tc is short for test calc
        self.tc = SC()

    def assert_state(self, exp_arith, exp_calc_text, exp_cur_text) -> None:
        self.assertEqual(exp_arith, self.tc.arith)
        self.assertEqual(exp_calc_text, self.tc.calculation_text.get())
        self.assertEqual(exp_cur_text, self.tc.current_text.get())

    def test_num(self):
        self.tc.number(1)
        self.assert_state(False, '', '0')


