# Given the head of a singly linked list,
# return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        middle = head
        while middle:
            middle = middle.next
            length += 1
        step = 0
        middle = head
        while step < length // 2:
            middle = middle.next
            step += 1
        return middle