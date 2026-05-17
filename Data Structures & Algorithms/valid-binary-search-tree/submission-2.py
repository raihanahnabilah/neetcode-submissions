# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, minVal, maxVal = queue.popleft()

            if not (minVal < node.val < maxVal):
                return False

            if node.left:
                queue.append((node.left, minVal, node.val))
            if node.right:
                queue.append((node.right, node.val, maxVal))
                
        return True


