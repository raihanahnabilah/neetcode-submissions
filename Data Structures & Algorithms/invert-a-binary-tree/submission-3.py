# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        def dfs(node):
            # Base case
            if node == None:
                return None

            # Recursion
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)


        
    


