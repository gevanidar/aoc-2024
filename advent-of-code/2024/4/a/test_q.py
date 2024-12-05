from q import getLines, solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        answer = solve(file_name)
        expected = 18
        self.assertEqual(answer, expected, "Incorrect")
       
    def test_1(self):
        file_name = "data_test_1.txt"
        answer = solve(file_name)
        expected = 18
        self.assertEqual(answer, expected, "Incorrect")

    def test_2(self):
        file_name = "data_test_2.txt"
        answer = solve(file_name)
        expected = 1
        self.assertEqual(answer, expected, "Incorrect")

    def test_3(self):
        file_name = "data_test_3.txt"
        answer = solve(file_name)
        expected = 2
        self.assertEqual(answer, expected, "Incorrect")

    def test_4(self):
        file_name = "data_test_4.txt"
        answer = solve(file_name)
        expected = 1
        self.assertEqual(answer, expected, "Incorrect")

    def test_5(self):
        file_name = "data_test_5.txt"
        answer = solve(file_name)
        expected = 3
        self.assertEqual(answer, expected, "Incorrect")

if __name__ == "__main__":
    unittest.main()
