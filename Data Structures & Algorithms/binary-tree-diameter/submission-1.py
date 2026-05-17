# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
    # Two solutions: DFS and BFS
        res = 0

        # With DFS
        def dfs(node):
            nonlocal res
            
            # Base case
            if node == None:
                return -1
            
            # Recursion
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            res = max(res, left + right)
            return max(left, right)

        dfs(root)

        return res



