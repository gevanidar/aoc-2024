from q import solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        output= solve(file_name)
        expected = 10092
        self.assertEqual(output, expected, "Incorrect")

    def test_1(self):
        file_name = "data_test_1.txt"
        output= solve(file_name)
        expected = 2028
        self.assertEqual(output, expected, "Incorrect")

if __name__ == "__main__":
    unittest.main()
