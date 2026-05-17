# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        # (0, 1) -> (1, 2) -> (2, 3)
        # (3, 2) -> (2, 1) -> (1, 0)

# when we're at 0
# we want to take value 0, then point next to None
# then we point to the next one which is 1

# when we're at 1
# we want to take value 1, then point next of new copy, which is 0
# then we point to the next one of the previous of original copy, which is 2

# and so on

# so basically:
# while there is head
# (1) store the prev head of the new one
# (2) store the new one
# (3) store the original copy
        prev, current = None, head

        while current:
            # print("CURRENT ", current.val)
            # I wanna save the actual current, to get the next one
            tmpCurrent = current
            tmpCurrentNext = current.next
            # print("TMP CURRENT ", tmpCurrentNext.val)
            # I wanna set the current.next to be the previous one
            current.next = prev
            current = tmpCurrentNext
            # print("CURRENT AFTER ", current.val)
            prev = tmpCurrent
            # print("CHECKING PREV ", prev.val)


        return prev



    