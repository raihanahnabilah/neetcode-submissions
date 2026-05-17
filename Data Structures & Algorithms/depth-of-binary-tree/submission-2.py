# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion - DFS
        # if root == None:
        #     return 0
        # else:
        #     left = self.maxDepth(root.left) + 1
        #     right = self.maxDepth(root.right) + 1
        #     return max(left, right)

        # # iteration - DFS - with stack
        # if root == None:
        #     return 0
        
        # rootList = [[root, 1]]
        # maxDepth = 0

        # while rootList:
        #     [currentRoot, depth] = rootList.pop()
        #     maxDepth = max(maxDepth, depth)
        #     if currentRoot.left:
        #         rootList.append([currentRoot.left, depth + 1])
        #     if currentRoot.right:
        #         rootList.append([currentRoot.right, depth + 1])
        # return maxDepth

        # iteration - BFS - with queue
        if root == None:
            return 0
        
        rootList = deque([root])
        maxDepth = 0
        while rootList:
            # for loop root list
            for _ in range(len(rootList)):
                currentRoot = rootList.popleft()
                if currentRoot.left:
                    rootList.append(currentRoot.left)
                if currentRoot.right:
                    rootList.append(currentRoot.right)
            maxDepth += 1
        return maxDepth

        



