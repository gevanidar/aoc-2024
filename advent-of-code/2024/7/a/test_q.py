from q import getLines, solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        answer = solve(file_name)
        expected = 3749
        self.assertEqual(answer, expected, "Incorrect")

    def test_1(self):
        file_name = "data_test_1.txt"
        answer = solve(file_name)
        expected = 6+7+8+12
        self.assertEqual(answer, expected, "Incorrect")

    def test_2(self):
        file_name = "data_test_2.txt"
        answer = solve(file_name)
        expected = (1+1+1)*2*4
        self.assertEqual(answer, expected, "Incorrect")

if __name__ == "__main__":
    unittest.main()
