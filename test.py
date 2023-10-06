from calculator import *
import unittest


class MyTestCase(unittest.TestCase):
    @ temp_change_state()
    def setUp(self) -> None:
        global arith, calculation_text, current_text
        arith = False
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, '0')

    # Test buttons by themselves
    def test_self_1(self):
        global arith, calculation_text, current_text
        button_click(1)
        self.assertFalse(arith)
        self.assertEqual(current_text.get(), '1')
        self.assertEqual(calculation_text.get(), '')
        button_click(3)
        self.assertFalse(arith)
        self.assertEqual(current_text.get(), '13')
        self.assertEqual(calculation_text.get(), '')

    def test_self_2(self):
        global arith, calculation_text, current_text
        arithmatic('+')
        self.assertEqual(current_text.get(), '0')
        self.assertEqual(calculation_text.get(), '0+')

    # Test number and arithmatic button together.
    def test_num_arith_1(self):
        global arith, calculation_text, current_text
        button_click(1)
        arithmatic('+')
        self.assertEqual(current_text.get(), '1')
        self.assertEqual(calculation_text.get(), '1+')

    def test_num_arith_2(self):
        global arith, calculation_text, current_text
        arithmatic('+')
        button_click(1)
        self.assertEqual(current_text.get(), '1')
        self.assertEqual(calculation_text.get(), '0+')

    def test_num_arith_3(self):
        global arith, calculation_text, current_text
        button_click(2)
        arithmatic('+')
        button_click(3)
        self.assertEqual(current_text.get(), '3')
        self.assertEqual(calculation_text.get(), '2+')


if __name__ == '__main__':
    unittest.main()
