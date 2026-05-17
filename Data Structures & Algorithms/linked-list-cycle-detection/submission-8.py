# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # About fast and slow pointer

        # 1, 2, 3, 4, 2
        # slow = moves once - 1, 2, 3
        # fast = moves twice - 1, 4, 3, meet!

        slow = fast = head

        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
