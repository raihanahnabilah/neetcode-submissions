# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Breadth first search: 1,2,3,4,5,6,7
        # Depth first search: 1,2,4,5,3,6,7

        # For DFS (using recursion):
        # Base case
        if root == None:
            return None
        # Recursive case 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

        # invertTree(3)
        # left = invertTree(1) = 1 
        # right = invertTree(2) = 2

        # invertTree(1)
        # left = invertTree(None) = None
        # right = invertTree(None) = None
        # return 1

        # invertTree(2)
        # left = invertTree(None) = None
        # right = invertTree(None)= None
        # return 2

        # invertTree(None)
        # return None 
