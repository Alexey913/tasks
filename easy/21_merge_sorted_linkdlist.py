# You are given the heads of two sorted
# linked lists list1 and list2.

# Merge the two lists into one sorted list.
# The list should be made by splicing together
# the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        if list1.val < list2.val:
            res = list1
        else:
            res = list2
        res = head
        while list1.val and list2.val:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
        return res