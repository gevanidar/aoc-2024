from typing import List, Optional
import statistics
import unittest
from q import Solution

class TestClass(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        s = [2]
        s = "babad"
        expected = "bab"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_1(self):
        solution = Solution()
        s = "cbbd"
        expected = "bb"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_2(self):
        solution = Solution()
        s = "cbbbbbbbbbbbdbbbbb"
        expected = "bbbbbbbbbbb"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_3(self):
        solution = Solution()
        s = "abcdefghijklmnopqstuvxyz"
        expected = "a"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")

    def test_4(self):
        solution = Solution()
        s = "ccc"
        expected = "ccc"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")
       
    def test_5(self):
        solution = Solution()
        s = "abb"
        expected = "bb"
        answer = solution.longestPalindrome(s)
        self.assertEqual(len(answer), len(expected), "Incorret answer.")
        if (False):
             self.assertEqual(answer, expected, "Incorret answer.")
       
       
if __name__ == "__main__":
    unittest.main()
