# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.


# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'


def revert_list(ll):
    previous_node = None
    current_node = ll
    next_node = ll.next
    while current_node.next:
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        next_node = current_node.next
    current_node.next = previous_node
    ll = current_node
    return ll


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num_1 = num_2 = 0
    step_1 = step_2 = 0
    new_l1 = revert_list(l1)
    l2 = revert_list(l2)
    while new_l1.next:
        num_1 += l1.val * 10 ** step_1
        print(num_1)
        l1 = l1.next
        step_1 += 1
    while l2.next:
        num_2 += l2.val * 10 ** step_2
        print(num_2)
        l2 = l2.next
        step_2 += 1

    return num_1 + num_2

three = ListNode(3, None)
two = ListNode(4,three)

l1 = ListNode(2, two)

six = ListNode(4, None)
five = ListNode(6, six)
l2 = ListNode(5, five)

print(l1)
print(revert_list(l1))
print(l2)
print(revert_list(l2))
print(addTwoNumbers(l1, l2))
