# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We can do slow and fast pointer! 
        slowPointer = fastPointer = head
        while slowPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer.val == fastPointer.val:
                return True
        return False