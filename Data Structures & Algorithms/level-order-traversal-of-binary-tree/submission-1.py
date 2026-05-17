# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # The BFS
        # Using queue

        res = []

        if root == None:
            return res

        queue = deque([root])

        while queue:
            lenLevel = len(queue)
            level = []

            for _ in range(lenLevel):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)            
                if currentNode.right:
                    queue.append(currentNode.right)
            res.append(level)
        
        return res



    # You have a queue
    # add 1 to the queue
    # while there is queue, keep doing this
    # currNode = 1
    # check if currNode has children:
    # append to the queue
    # queue.append(2) queue.append(3)
    # for node in queue:
    # popleft 


            