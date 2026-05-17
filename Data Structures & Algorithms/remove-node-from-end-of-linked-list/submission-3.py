# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find the length
        length = 0
        length_pointer = head
        while length_pointer.next:
            length += 1
            length_pointer = length_pointer.next
        length += 1

        # index we need to go to:
        index = length - n

        remove_pointer = head
        result = remove_pointer
        # traverse to that index 
        # if it's at the beginning
        if index == 0:
            return remove_pointer.next

        # if it's in the middle or the end 
        while remove_pointer and remove_pointer.next:
            index -= 1
            # removal
            if index == 0:
                index -= 1
                # store the next node of the node after current
                next_node = remove_pointer.next.next
                # cut it
                remove_pointer.next = next_node
            remove_pointer = remove_pointer.next
        
        return result




            