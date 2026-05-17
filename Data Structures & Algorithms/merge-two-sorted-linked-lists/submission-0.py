# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Need to create a dummy!
        head = node = ListNode() 

        while list1 and list2:
            if list1.val < list2.val:
                # Setting list 1 to be the .next of the previous one if any
                node.next = list1
                # Go to the next one
                list1 = list1.next

                node = node.next

            elif list1.val > list2.val:
                node.next = list2
                # go to the next one
                list2 = list2.next
                
                node = node.next

            else:
                node.next = list1
                node = node.next
                list1 = list1.next

                node.next = list2
                node = node.next

                list2 = list2.next
                print("list1", list1)
                print("list2", list2)
        
        while list1:
            node.next = list1
            list1 = list1.next
            node = node.next
        
        while list2:
            node.next = list2
            list2 = list2.next
            print("list2 there", list2)
            node = node.next


        return head.next
            