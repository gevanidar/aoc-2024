from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index0 = 0
        index1 = len(nums) - 1

        sorted_nums = sorted(nums)

        while True:
            num0 = sorted_nums[index0]
            num1 = sorted_nums[index1]
            value = num0 + num1
            same = num0 == num1
            if (value == target):
                if num0 < 0:
                    real_index0 = nums.index(num0)
                    if same:
                        nums.pop(real_index0)
                    real_index1 = nums.index(num1) 
                    if num0 == num1:
                        return [real_index0, real_index1 + 1]
                    return [real_index0, real_index1]
                else:
                    real_index0 = nums.index(num0)
                    if same:
                        nums.pop(real_index0)
                    real_index1 = nums.index(num1)
                    if same:
                        return [real_index0, real_index1 + 1]
                    return [real_index0, real_index1]
            elif value < target:
                index0 += 1
            else:
                index1 -= 1

