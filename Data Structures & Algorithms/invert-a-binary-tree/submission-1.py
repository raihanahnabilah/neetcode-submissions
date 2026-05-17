# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # You can do either recursion or iteration here
        # # With recursion:

        # if root == None:
        #     return root

        # # Root condition
        # if root.left == None and root.right == None:
        #     return root
        # # Recursive condition
        # else:
        #     # Go to left and right tree
        #     leftRoot = self.invertTree(root.left)
        #     rightRoot = self.invertTree(root.right)
        #     root.right = leftRoot
        #     root.left = rightRoot
        #     return root


        # With breadth first search using stack
        if root == None:
            return root
        rootList = [root]
        while rootList:
            currentRoot = rootList.pop()
            if currentRoot.left:
                rootList.append(currentRoot.left)
            if currentRoot.right:    
                rootList.append(currentRoot.right)
            tmpLeft = currentRoot.left
            tmpRight = currentRoot.right
            currentRoot.left = tmpRight
            currentRoot.right = tmpLeft
        return root











            