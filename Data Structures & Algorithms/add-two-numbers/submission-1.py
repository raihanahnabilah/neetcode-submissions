# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = res = ListNode()
        prev_total = 0
        while l1 and l2:
            curr_total = prev_total + l1.val + l2.val
            if len(str(curr_total)) > 1:
                prev_total = int(str(curr_total)[0])
                curr_total = int(str(curr_total)[-1])
            else:
                prev_total = 0
            new_node = ListNode(curr_total)
            res.next = new_node
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_total = prev_total + l1.val
            if len(str(curr_total)) > 1:
                prev_total = int(str(curr_total)[0])
                curr_total = int(str(curr_total)[-1])
            else:
                prev_total = 0
            new_node = ListNode(curr_total)
            res.next = new_node
            res = res.next
            l1 = l1.next

        while l2:
            curr_total = prev_total + l2.val
            if len(str(curr_total)) > 1:
                prev_total = int(str(curr_total)[0])
                curr_total = int(str(curr_total)[-1])
            else:
                prev_total = 0
            new_node = ListNode(curr_total)
            res.next = new_node
            res = res.next
            l2 = l2.next

        if prev_total:
            new_node = ListNode(prev_total)
            res.next = new_node
            res = res.next

        return head.next



