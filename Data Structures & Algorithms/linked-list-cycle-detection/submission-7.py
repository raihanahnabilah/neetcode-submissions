# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        if head is None or head.next is None:
            return False

        while fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                return True
  
        return False