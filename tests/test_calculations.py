import unittest
from mathlib.calculations import add, subtract, multiply, divide

class TestCalculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Cannot divide by zero")
        self.assertEqual(divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()