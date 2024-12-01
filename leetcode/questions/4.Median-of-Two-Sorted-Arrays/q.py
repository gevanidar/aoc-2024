from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        elements = len(nums1) + len(nums2)
        even = elements % 2 == 0
        middle = (elements - 1) / 2

        while middle >= 1:
            if len(nums1) == 0 or len(nums2) == 0:
                break
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
            middle -= 1
        middle = int(middle // 1)
        if len(nums1) == 0:
            if even:
                return (nums2[middle] + nums2[middle+1]) / 2
            else:
                return nums2[middle]
        elif len(nums2) == 0:
            if even:
                return (nums1[middle] + nums1[middle+1]) / 2
            else:
                return nums1[middle]
        else:
            if even:
                values = []
                values = [nums1[middle], nums2[middle]]
                if len(nums1) > 1:
                    values.append(nums1[middle+1])
                if len(nums2) > 1:
                    values.append(nums2[middle+1])
                values.sort()
                print(f'{values=}, {values[:2]=}')
                return sum(values[:2]) / 2
            else:
                return min(nums1[middle], nums2[middle])
                      
