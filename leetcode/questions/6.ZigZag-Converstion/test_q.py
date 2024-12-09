from typing import List, Optional
import statistics
import unittest
from q import Solution

class TestClass(unittest.TestCase):

    def test_0(self):
        solution = Solution()
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        answer = solution.convert(s, numRows)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_1(self):
        solution = Solution()
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        answer = solution.convert(s, numRows)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_2(self):
        solution = Solution()
        s = "A"
        numRows = 1
        expected = "A"
        answer = solution.convert(s, numRows)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_4(self):
        solution = Solution()
        s = "ABC"
        numRows = 2
        expected = "ACB"
        answer = solution.convert(s, numRows)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_4(self):
        solution = Solution()
        s = "AB"
        numRows = 1
        expected = "AB"
        answer = solution.convert(s, numRows)
        checkLength = False
        if checkLength:
            self.assertEqual(len(answer), len(expected), "Incorret answer.")
        else:
             self.assertEqual(answer, expected, "Incorret answer.")



      
if __name__ == "__main__":
    unittest.main()
