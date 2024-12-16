from q import solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        answer = solve(file_name)
        expected = 1930
        self.assertEqual(answer, expected, "Incorrect")

    def test_1(self):
        file_name = "data_test_1.txt"
        answer = solve(file_name)
        expected = 140
        self.assertEqual(answer, expected, "incorrect")


if __name__ == "__main__":
    unittest.main()
