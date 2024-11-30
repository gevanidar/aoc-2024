from typing import List, Optional
import unittest
from q import Solution

class TestClass(unittest.TestCase):

        
        

    def test_sum_0(self):
        solution = Solution()
        s = "abcabcbb"
        expected = 3
        answer = solution.lengthOfLongestSubstring(s)
        self.assertEqual(answer, expected, "Incorret answer.")


    def test_sum_1(self):
        solution = Solution()
        s = "bbbbb"
        expected = 1
        answer = solution.lengthOfLongestSubstring(s)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_2(self):
        solution = Solution()
        s = "pwwkew"
        expected = 3
        answer = solution.lengthOfLongestSubstring(s)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_3(self):
        solution = Solution()
        s = " "
        expected = 1
        answer = solution.lengthOfLongestSubstring(s)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_4(self):
        solution = Solution()
        s = "aabaab!bb"        
        expected = 3
        answer = solution.lengthOfLongestSubstring(s)
        self.assertEqual(answer, expected, "Incorret answer.")
        
    
if __name__ == "__main__":
    unittest.main()
