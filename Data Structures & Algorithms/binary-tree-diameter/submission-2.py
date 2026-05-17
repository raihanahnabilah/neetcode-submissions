# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Two solutions: DFS and BFS
        # With DFS
        def dfs(node):
            # Base case
            if node == None:
                return (-1, 0)
            
            # Recursion
            left, maxLeft = dfs(node.left)
            right, maxRight = dfs(node.right)
            return (max(left + 1, right + 1), max(maxLeft, maxRight, left + right + 2))

        return dfs(root)[1]



