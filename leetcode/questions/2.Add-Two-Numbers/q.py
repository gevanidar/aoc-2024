from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getValue(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        value = l1.val
        if l1.next == None:
            return value
        power = 10
        node = l1.next
        while True:
            val = node.val
            value += val * power
            power *= 10
            node = node.next
            if node == None:
                break
        return value

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1
        values = [self.getValue(l1), self.getValue(l2)]
        value = sum(values)
        l3 = []
        while value >= 1:
            remainder = value % 10
            l3.append(remainder)
            value = value // 10
            

        return self.buildLinkedList(l3)

        
    def buildLinkedList(self, values):
        first = values[0]
        rest = values[1:]
        listNode = ListNode(values[0])
        if len(values) == 1:
            return listNode
        listNode.next = self.buildLinkedList(rest)
        return listNode

