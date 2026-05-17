# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxVal = 0

        def dfs(root):
            nonlocal maxVal
            if root == None:
                return -1
            else:
                left = dfs(root.left) + 1
                right = dfs(root.right) + 1
                maxVal = max(maxVal, left + right)
                return max(left, right)

        dfs(root)
        return maxVal



            