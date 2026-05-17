# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # You can do either recursion or iteration here
        # With recursion:

        if root == None:
            return root

        # Root condition
        if root.left == None and root.right == None:
            return root
        # Recursive condition
        else:
            # Go to left and right tree
            leftRoot = self.invertTree(root.left)
            rightRoot = self.invertTree(root.right)
            root.right = leftRoot
            root.left = rightRoot
            return root



        # while root.left and root.right:
        #     tmpLeft = root.left
        #     tmpRight = root.right
        #     root.right = tmpLeft
        #     root.left = tmpRight
            
        #     # lets go to left first
        #     root = root.left

        #     # then lets go to right
            