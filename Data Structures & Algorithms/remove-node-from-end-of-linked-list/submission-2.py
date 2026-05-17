# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Traverse through the node 
        newHead = head

        length = 0
        while newHead:
            length += 1
            newHead = newHead.next

        indexTarget = length - n

        if indexTarget == 0:
            return head.next
            
        counter = 0
        headCopy = head
        while headCopy:
            counter += 1
            if counter == indexTarget:
                headCopy.next = headCopy.next.next
                headCopy = headCopy.next
            else:
                headCopy = headCopy.next            
        return head








