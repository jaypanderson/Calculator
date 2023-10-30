import unittest
from calculator import SimpleCalc as sc
import customtkinter as ctk



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # tc is short for test calc
        self.root = ctk.CTk()
        self.tc = sc(self.root)
    def assert_state(self, exp_arith, exp_calc_text, exp_cur_text) -> None:
        self.assertEqual(exp_arith, self.tc.arith)
        self.assertEqual(exp_calc_text, self.tc.calculation_text.get())
        self.assertEqual(exp_cur_text, self.tc.current_text.get())

    def test_num(self):
        self.tc.number(1)
        self.assert_state(False, '', '1')

if __name__ == '__main__':
    unittest.main()


