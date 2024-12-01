from typing import List, Optional
import statistics
import unittest
from q import Solution

class TestClass(unittest.TestCase):
    def test_sum_0(self):
        solution = Solution()
        nums1 = [1,3]
        nums2 = [2]
        expected = 2.00000
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")
       
    def test_sum_1(self):
        solution = Solution()
        nums1 = [1,2]
        nums2 = [3,4]
        expected = 2.50000
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_2(self):
        solution = Solution()
        nums1 = [1,2,3,4]
        nums2 = []
        expected = 2.50000
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_3(self):
        solution = Solution()
        nums1 = [1,2,3,4]
        nums2 = [5]
        expected = 3.00000
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_4(self):
        solution = Solution()
        nums1 = [i for i in range(3, 100, 3)]
        nums2 = [i for i in range(3, 100, 5)]
        nums3 = []
        for i in nums1:
            nums3.append(i)
        for i in nums2:
            nums3.append(i)
        expected = statistics.median(nums3)
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")

    def test_sum_5(self):
        solution = Solution()
        nums1 = [i for i in range(1, 10000, 3)]
        nums1.append(10000000)
        nums1.append(10000000)
        nums1.append(10000000)
        nums2 = [i for i in range(3, 100, 5)]
        nums3 = []
        for i in nums1:
            nums3.append(i)
        for i in nums2:
            nums3.append(i)
        expected = statistics.median(nums3)
        answer = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, expected, "Incorret answer.")


if __name__ == "__main__":
    unittest.main()
