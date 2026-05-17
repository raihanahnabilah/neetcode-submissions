# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # fast and slow pointer:
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # the mid point stops right at slow
        #[2,4,6 (slow), 8, 10]

        # so now we wanna cut it in half
        curr = slow.next
        slow.next = None
        # [2,4,6] [8,10]

        # and we wanna reverse the curr
        # 8->10
        # steps:
        # store 10
        # None <- 8, 
        # move to 10
        # prev becomes 8
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # already reversed to [10, 8]
        # result: prev

        # [2,4,6] [10,8]
        # [2,10,4,8,6]
        # so now we wanna combine both?
        while head and prev:
            head_nxt = head.next # store next for head - 4
            prev_nxt = prev.next # store next for prev - 8
            head.next = prev # 2 -> 10
            prev.next = head_nxt # 2 -> 10 -> 4
            head = head_nxt # 4
            prev = prev_nxt # 8
            









            