# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find midpoint
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # midpoint is at slow now
        # cut list from midpoint
        head2 = slow # pointing at midpoint
        head2 = head2.next # start of second list
        slow.next = None

        # 4-> 5-> 6
        # None <- 4 
        # reverse second list
        prevNode = None
        while head2:
            # storing next value (5)
            nextNode = head2.next 
            # pointing the head to None (4 now points to None)
            head2.next = prevNode 
            # prevNode should now be the currentNode
            prevNode = head2
            # pointing head2 to the nextNode (5)
            head2 = nextNode

        
        # to reorder:
        head1 = head
        head2 = prevNode
        # head = newNode = ListNode()

        # 0,1,2,3
        # 6,5,4

        # 0-> 6
        # 1,2,3
        # 6,5,4
        while head1 and head2:
            # store the next nodes
            next1 = head1.next
            next2 = head2.next
            # point new ones:
            head1.next = head2
            head2.next = next1
            # move ll1 and ll2
            head1 = next1
            head2 = next2


            

        


        
