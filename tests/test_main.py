import unittest
from utils.helpers import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("world"), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
