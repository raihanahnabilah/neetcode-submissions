# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headToCountLength = head
        
        # Traverse to find length
        length = 0 
        while headToCountLength: # O(n)
            length += 1
            headToCountLength = headToCountLength.next
            
        # edge case
        if n == length:
            return head.next

        # Remove the nth node
        dummy = head
        counter = 1
        while counter < (length - n):
            dummy = dummy.next
            counter += 1
        
        # once you found the counter
        dummy.next = dummy.next.next

        return head



