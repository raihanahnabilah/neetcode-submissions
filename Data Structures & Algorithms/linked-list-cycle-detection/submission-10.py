# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Cycle means = if you have fast and slow pointer, it'll 
        # point to the same value at some point
        # Otherwise, it'll point to null

        fast = slow = head

        while slow.next and fast.next:
            slow = slow.next
            if not fast.next.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False





