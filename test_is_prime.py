import unittest
from is_prime import is_prime
class TestIsPrimeFunction(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))


if __name__ == "__main__":
    unittest.main()
