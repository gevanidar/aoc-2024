from typing import List, Optional
import unittest
from q import Solution, ListNode


class TestClass(unittest.TestCase):

    def compareLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        while l1.next != None and l2.next != None:
            self.assertEqual(l1.val, l2.val, "Incorrect value")
            l1 = l1.next
            l2 = l2.next
            #print(l1.val, l1.next, l2.val, l2.next)
        self.assertEqual(l1.next, None, "l1 not at last element")
        self.assertEqual(l2.next, None, "l2 not at last element")
        
        

    def test_sum_0(self):
        solution = Solution()
        l1 = [2,4,3]
        l2 = [5,6,4]
        expected = [7,0,8]
        listNodes1 = solution.buildLinkedList(l1)
        listNodes2 = solution.buildLinkedList(l2)
        listNodesExpected = solution.buildLinkedList(expected)
        answer = solution.addTwoNumbers(listNodes1, listNodes2)
        self.compareLists(listNodesExpected, answer)

    def test_sum_1(self):
        solution = Solution()
        l1 = [0]
        l2 = [0]
        expected = [0]
        listNodes1 = solution.buildLinkedList(l1)
        listNodes2 = solution.buildLinkedList(l2)
        listNodesExpected = solution.buildLinkedList(expected)
        answer = solution.addTwoNumbers(listNodes1, listNodes2)
        self.compareLists(listNodesExpected, answer)

    def test_sum_2(self):
        solution = Solution()
        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        listNodes1 = solution.buildLinkedList(l1)
        listNodes2 = solution.buildLinkedList(l2)
        listNodesExpected = solution.buildLinkedList(expected)
        answer = solution.addTwoNumbers(listNodes1, listNodes2)
        self.compareLists(listNodesExpected, answer)

    def test_sum_3(self):
        solution = Solution()
        l1 = [0,8,6,5,6,8,3,5,7]    
        l2 = [6,7,8,0,8,5,8,9,7]
        expected = [6,5,5,6,4,4,2,5,5,1]
        listNodes1 = solution.buildLinkedList(l1)
        listNodes2 = solution.buildLinkedList(l2)
        listNodesExpected = solution.buildLinkedList(expected)
        answer = solution.addTwoNumbers(listNodes1, listNodes2)
        self.compareLists(listNodesExpected, answer)

if __name__ == "__main__":
    unittest.main()
