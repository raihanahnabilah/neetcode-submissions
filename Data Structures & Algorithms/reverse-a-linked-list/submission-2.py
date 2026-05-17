# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # # Solution 1:
        # # Store all the values in an array
        # vals = [] # O(n) space complexity
        # while head and head.next: # O(n) time complexity
        #     vals.append(head.val)
        #     head = head.next
        
        # if head:
        #     vals.append(head.val)

        # print(vals)

        # newHead = newList = ListNode() # O(n) space complexity
        # for i in range(len(vals)-1, -1, -1): # O(n) time complexity
        #     newNode = ListNode(vals[i])
        #     newList.next = newNode
        #     newList = newList.next
        
        # return newHead.next

        # Solution 2:
        copy = head
        prevNode = None
        while head:
            # 1-> 2 -> 3
            # <- 1

            # current is 1
            nextNode = head.next # this will be 2
            head.next = prevNode # 1 is now pointing to None
            prevNode = head # prevNode is now 1
            head = nextNode # update current node to 2
        return prevNode


            



