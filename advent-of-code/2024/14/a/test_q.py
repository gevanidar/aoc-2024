from q import solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        width = 11
        height = 7
        answer = solve(file_name, width, height)
        expected = 12
        self.assertEqual(answer, expected, "Incorrect")


if __name__ == "__main__":
    unittest.main()
