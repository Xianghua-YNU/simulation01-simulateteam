import unittest
from fac import factorial

class TestFacFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
if __name__ == "__main__":
    unittest.main()
