"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1
        # 2 3
        # 4.  5
        # With BFS
        # Lets say I have this [[2, 3], [1,4], [1, 5], [2], [3]]
        # that means with BFS, the order is 1 2 3 4 5
        # Node n = 1 -> [2,3] -> append in the neighbors for the new node
        # Node n = 1, neighbors = [Node(2),Node(3)] -> check length: 2 -> for i in range(len(neighbors))
        # Node n = 2 -> [3,1,4] # but 1 is already visited, so make sure to not visit again -> add 1,4 to the queue
        # Node n = 3 -> [1, 4, 1, 5] # but 1 is already visited, so make sure to not visit again

        if node == None:
            return None

        oldToNewGraph = {}

        def bfs(root):
            queue = deque([root])
            oldToNewGraph[root] = Node(root.val)

            while queue:
                currentNode = queue.popleft()

                for i in range(len(currentNode.neighbors)):
                    currentNeighbor = currentNode.neighbors[i]
                    if currentNeighbor not in oldToNewGraph:
                        oldToNewGraph[currentNeighbor] = Node(currentNeighbor.val)
                        queue.append(currentNeighbor)
                    oldToNewGraph[currentNode].neighbors.append(oldToNewGraph[currentNeighbor])


        bfs(node)
        return oldToNewGraph[node]

