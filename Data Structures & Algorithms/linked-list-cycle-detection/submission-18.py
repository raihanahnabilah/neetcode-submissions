# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # this can do with fast and slow pointer
        # fast pointer: moves 2x
        # slow pointer: moves 1x

        #1,1
        #2,3
        #3,2
        #4,4 = same

        # time complexity: O(n)
        # space complexity: O(1)

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False