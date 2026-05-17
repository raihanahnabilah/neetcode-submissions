# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1,2,4
        # 1,3,5

        # compare 1 and 1:
        # 1 -> 1
        # compare 2 and 3:
        # 1 -> 1 -> 2 -> 3
        # compare 4 and 5:
        # 1 -> 1 -> 2 -> 3 -> 4 -> 5

        # edge cases:
        # what if first list is more than second list?
        # are each list are already sorted to begin with?

        # 1,2,4,6
        # 1,3,5
        # just add the remaining

        head = newList = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next 

        if list2:
            while list2:
                newList.next = list2
                list2 = list2.next
                newList = newList.next

        if list1:
            while list1:
                newList.next = list1
                list1 = list1.next
                newList = newList.next

        return head.next



