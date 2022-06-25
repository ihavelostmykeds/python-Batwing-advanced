import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculatorTest = Calculator()

    def test_calculator_add(self):
        self.assertEqual(self.calculatorTest.add(2, 3), 5)

    def test_calculator_substract(self):
        self.assertEqual(self.calculatorTest.subtract(3, 2), 1)

    def test_calculator_multiply(self):
        self.assertEqual(self.calculatorTest.multiply(3, 2), 6)

    def test_calculator_divide(self):
        self.assertEqual(self.calculatorTest.divide(4, 2), 2)
        with self.assertRaises(ValueError):
            self.calculatorTest.divide(4, 0)


    