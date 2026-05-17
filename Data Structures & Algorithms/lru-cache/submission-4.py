class Node:
    def __init__(self, k = -1, v = -1, prev = None, ne = None):
        self.key = k
        self.val = v
        self.prevNode = prev
        self.nextNode = ne

class LRUCache:
    def __init__(self, capacity: int):
        self.root = Node()
        self.cache = {}
        self.capacity = capacity

        self.left = Node()
        self.right = Node()
        # Setting left and right to be prev and next of each other
        self.left.nextNode, self.right.prevNode = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove first from the linkedlist
            self.remove(self.cache[key])
            # Reinsert to the last node
            self.insert(self.cache[key]) 
            return self.cache[key].val
        return -1

    # Insert at the end of doubly linkedlist
    def insert(self, newNode):
        rightPrev = self.right.prevNode
        self.right.prevNode = newNode
        newNode.nextNode = self.right
        rightPrev.nextNode = newNode
        newNode.prevNode = rightPrev

    def remove(self, node):
        prev, nxt = node.prevNode, node.nextNode
        prev.nextNode, nxt.prevNode = nxt, prev

    def put(self, key: int, value: int) -> None:        
        if key in self.cache:
            self.remove(self.cache[key]) # remove from wherever it is to the end
        
        #If it's not in cache
        newNode = Node(key,value)
        # Basically initially we have:
        # left = Node(-1,-1), right = Node(-1,-1)
        # When we insert:
        # rightPrev = newNode
        # newNodeNext = right
        # leftNext = newNode
        # newNodePrev = left
        self.cache[key] = newNode
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove the left.next node
            lru = self.left.nextNode
            self.remove(lru)
            del self.cache[lru.key]




