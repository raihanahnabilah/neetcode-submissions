# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # There's DFS and BFS
        # DFS -> You do recursion

        # Base case
        # If currNode == None
        # return 0

        # Recursion
        # left = dfs(currNode.left) + 1
        # right = dfs(currNode.right) + 1
        # return max(left, right)

        # def dfs(currNode):
        #     if currNode == None:
        #         return 0

        #     left = dfs(currNode.left) + 1
        #     right = dfs(currNode.right) + 1
        #     return max(left, right)
        
        # return dfs(root)

        # BFS -> Checking the level??

        res = 0

        if root == None:
            return res

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            res += 1
        
        return res



        
        

