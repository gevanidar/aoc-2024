import unittest
from q import Solution

class TestClass(unittest.TestCase):
    def test_sum_0(self):
        solution = Solution()
        nums = [2,7,11,15]
        target = 9
        expected = [0,1]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")
    
    def test_sum_1(self):
        solution = Solution()
        nums = [3,2,4]
        target = 6
        expected = [1,2]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")
    
    def test_sum_2(self):
        solution = Solution()
        nums = [3,3]
        target = 6
        expected = [0,1]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")

    def test_sum_2(self):
        solution = Solution()
        nums = [3,3]
        target = 6
        expected = [0,1]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")

    def test_sum_3(self):
        solution = Solution()
        nums = [-1,-2,-3,-4,-5]
        target = -8
        expected = [2,4]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")

    def test_sum_4(self):
        solution = Solution()
        nums = [5, 75, 25]
        target = 100
        expected = [1, 2]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")

    def test_sum_5(self):
        solution = Solution()
        nums = [2, 2, 1]
        target = 4
        expected = [0, 1]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")
        
    def test_sum_6(self):
        solution = Solution()
        nums = [-500000000,2,4,-500000000]
        target = -1000000000
        expected = [0, 1]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")
        
    def test_sum_6(self):
        solution = Solution()
        nums = [3,2,3]
        target = 6
        expected = [0, 2]
        answer = solution.twoSum(nums, target)
        answer.sort()
        self.assertEqual(expected, answer, "Incorrect value")

if __name__ == "__main__":
    unittest.main()
