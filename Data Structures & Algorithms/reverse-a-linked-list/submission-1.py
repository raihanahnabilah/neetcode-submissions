# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Store all the values in an array
        vals = []
        while head and head.next:
            vals.append(head.val)
            head = head.next
        
        if head:
            vals.append(head.val)
            
        print(vals)

        newHead = newList = ListNode()
        for val in vals[::-1]:
            newNode = ListNode(val)
            newList.next = newNode
            newList = newList.next
        
        return newHead.next

            



