from q import solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        steps = 25
        answer = solve(file_name, steps)
        expected = 55312
        self.assertEqual(answer, expected, "Incorrect")

    def test_1(self):
        file_name = "data_test_0.txt"
        steps = 6
        answer = solve(file_name, steps)
        expected = 22
        self.assertEqual(answer, expected, "Incorrect")
   

if __name__ == "__main__":
    unittest.main()
