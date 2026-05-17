"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        #   1
        #  2. 3
        # 4     5
        # Initially:
        # [[2, 3], [1, 4], [1, 5], [2], [3]]
        # 
        # With BFS
        # Node(val = 1, neighbors = [2,3])
        # Mark 1 as visited
        # [2, 3] -> Add 2 and 3 to queue and to the neighbors
        # Node (val = 2, neighbors = [1, 4])
        # Mark 2 as visited
        # [1, 4] -> 1 is already visited, so no need to visit again, add 4 to the queue
        # Node (val = 3, neighbors = [1,5])
        # Mark 3 as visited
        # [1, 5] -> 1 is already visited, so no need to visit again, add 5 to the queue
        # Node (val = 4, neighbors = [2])
        # Mark 4 as visited

        if node == None:
            return None
        

        val_to_new_node = {} 
        queue = deque([node])
        # cloned graph
        val_to_new_node[node.val] = Node(node.val)
        
        while queue:
            # Current node
            currentNode = queue.popleft()

            for neighbor in currentNode.neighbors:
                if neighbor.val in val_to_new_node:
                    val_to_new_node[currentNode.val].neighbors.append(val_to_new_node[neighbor.val])
                else:
                    val_to_new_node[neighbor.val] = Node(neighbor.val)
                    val_to_new_node[currentNode.val].neighbors.append(val_to_new_node[neighbor.val])
                    queue.append(neighbor)
        
        return val_to_new_node[node.val]






        

        

