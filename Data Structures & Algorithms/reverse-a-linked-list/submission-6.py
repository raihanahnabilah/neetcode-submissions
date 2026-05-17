# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> None
        # None <- 0 / 1 -> 2 -> 3

        # save the next value of 0 (currNext)
        # point prev 0 to None
        # update 0 as the prev
        # curr moves to 1

        prev = None
        curr = head
        
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext

        return prev 

