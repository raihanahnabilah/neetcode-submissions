# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1,2,3,4

        # time complexity: O(n)
        # space complexity: O(1)
        
        length = 0
        counter_pointer = head
        # first step count the number of items in LL
        # we've counted that length = 4
        while counter_pointer:
            length += 1
            counter_pointer = counter_pointer.next
        
        # index to remove from top:
        index_to_remove = length - n

        if index_to_remove == 0:
            return head.next

        curr = head
        curr_position = 0

        while curr:
            if index_to_remove == curr_position + 1:
                if length - 1 == curr_position + 1:
                    curr.next = None
                    return head
                else:     
                    curr.next = curr.next.next
            curr = curr.next
            curr_position += 1
        return head
        




