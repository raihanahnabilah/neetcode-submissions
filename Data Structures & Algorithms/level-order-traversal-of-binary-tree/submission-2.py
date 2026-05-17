# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # time complexity: O(n)
        # space complexity: O(n)

        # this is bfs
        res = []
        if not root:
            return res

        queue = deque([])
        queue.append(root)

        while queue:
            level_length = len(queue)
            temp = []
            for _ in range(level_length):
                curr_node = queue.popleft()
                temp.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(temp)

        return res





