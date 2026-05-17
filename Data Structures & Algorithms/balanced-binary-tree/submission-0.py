# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def dfs(root):
            nonlocal res

            # recursion - DFS
            if root == None:
                return -1
            else:
                left = dfs(root.left) + 1
                right = dfs(root.right) + 1
                if (abs(right-left)) > 1:
                    res = False
                return max(left, right)
        
        dfs(root)
        return res

