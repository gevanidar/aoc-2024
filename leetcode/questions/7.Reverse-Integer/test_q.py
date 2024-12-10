from typing import List, Optional
import statistics
import unittest
from q import Solution
import math

class TestClass(unittest.TestCase):

    def test_0(self):
        solution = Solution()
        x = 123
        expected = 321
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_1(self):
        solution = Solution()
        x = -123
        expected = -321
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

      
    def test_2(self):
        solution = Solution()
        x = 120
        expected = 21
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_3(self):
        solution = Solution()
        x = 100000
        expected = 1
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_4(self):
        solution = Solution()
        x = math.pow(2, 31)
        expected = 0 # Too large
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_5(self):
        solution = Solution()
        x = - math.pow(2, 31) - 1
        expected = 0 # Too negatively large
        answer = solution.reverse(x)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

if __name__ == "__main__":
    unittest.main()
