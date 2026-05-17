"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}

        # first traversal just to copy the data
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        # second traversal, to do the pointing
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = None if curr.next is None else oldToCopy[curr.next]
            copy.random = None if curr.random is None else oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head] if head is not None else None
        
        





