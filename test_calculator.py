import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add_returns11ForSummands1and10(self):
        calculator = Calculator()
        result = calculator.add(1, 10)
        self.assertEqual(11, result)

    def test_add_returns15ForSummands7and8(self):
        calculator = Calculator()
        result = calculator.add(7, 8)
        self.assertEqual(15, result)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(12, 3)
        self.assertEqual(9, result)

    def test_subtract_OtherNumbers(self):
        calculator = Calculator()
        result = calculator.subtract(16, 9)
        self.assertEqual(7, result)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(12, 3)
        self.assertEqual(36, result)

    def test_multiply_OtherNumbers(self):
        calculator = Calculator()
        result = calculator.multiply(7, 9)
        self.assertEqual(63, result, "Result of multiplication of 7 and 9 is 63")

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(12, 3)
        self.assertEqual(4, result)

    def test_divide_OtherNumbers(self):
        calculator = Calculator()
        result = calculator.divide(81, 9)
        self.assertEqual(9, result)
