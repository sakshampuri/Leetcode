# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        prev = head
        head = head.next if head and head.next else head
        while head and head.next:
            if prev == head:
                return True
            prev, head = prev.next, head.next.next
        return False