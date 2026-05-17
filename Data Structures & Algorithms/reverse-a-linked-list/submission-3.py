# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head: 0 -> 1 -> 2 -> 3 -> None
        # result: 3 -> 2 -> 1 -> 0 -> None

        # stores next value 1
        # 0 -> None
        prev = None

        while head:
            # stores next value 
            nextNode = head.next # stores 1
            # points current value to prev
            head.next = prev # points 0 to None
            # moves prev to current head?
            prev = head # now 0
            # moves head to next
            head = nextNode # now 1

        return prev
