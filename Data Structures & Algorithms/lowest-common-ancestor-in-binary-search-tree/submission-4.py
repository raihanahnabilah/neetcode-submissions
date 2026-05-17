# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # time complexity: O(logn)
        # space complexity: O(logn) -because of recursion

        # left -> found
        # right -> found
        # if left == found & right == found, then we return the root val
        
        # pTrue, qTrue
        def recurse(node):
            # base case
            if not node or not p or not q:
                return None
            
            # recursive case


            # if p and q is larger than current node, then we wanna make sure we go to the right
            if min(p.val, q.val) > node.val:
                return recurse(node.right)

            # if p and q is smaller than current node, then we wanna make sure we go to the left
            if max(p.val, q.val) < node.val:
                return recurse(node.left)

            # say value is 3 and 8
            # we know that 3 < 5, and 8 > 5
            # so that means the root is the result
            return node


        return recurse(root)

