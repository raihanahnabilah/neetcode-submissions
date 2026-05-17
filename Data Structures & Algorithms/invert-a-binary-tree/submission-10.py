# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # # dfs
        # # time complexity: O(n) - all nodes are traversed
        # # space complexity: O(n) - for recursion stack

        # if root is None:
        #     return            
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # bfs
        # time complexity: O(n)
        # space complexity: O(n)
        if root is None:
            return None

        queue = deque([])
        queue.appendleft(root)

        while queue:
            curr_root = queue.popleft()
            curr_root.left, curr_root.right = curr_root.right, curr_root.left
            if curr_root.left:
                queue.appendleft(curr_root.left)
            if curr_root.right:
                queue.appendleft(curr_root.right)
        
        return root

            
        

