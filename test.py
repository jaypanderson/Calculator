from calculator import *
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        global arith, calculation_text, current_text
        arith = False
        calculation_text.delete(0, END)
        current_text.delete(0, END)
        current_text.insert(0, '0')

    # test number buttons
    def test_1(self):
        global arith, calculation_text, current_text
        button_click(1)
        self.assertEqual(current_text.get(), '1')

    def test_2(self):
        global arith, calculation_text, current_text
        arithmatic('+')
        self.assertEqual(current_text.get(), '0')
        self.assertEqual(calculation_text.get(), '0+')


if __name__ == '__main__':
    unittest.main()
