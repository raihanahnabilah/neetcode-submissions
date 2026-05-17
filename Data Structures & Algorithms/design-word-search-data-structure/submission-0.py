class Node:
    def __init__(self):
        self.child = [None] * 26
        self.completed = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        currNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            # If it doesnt exist, then u just append
            if currNode.child[index] == None:
                newNode = Node()
                currNode.child[index] = newNode
            currNode = currNode.child[index]
        currNode.completed = True

    def search(self, word: str) -> bool:
        def dfs(newIndex, node):
            currNode = node

            for i in range(newIndex, len(word)):
                char = word[i]
                if char == ".":
                    for nodeChild in currNode.child:
                        if nodeChild is not None:
                            if dfs(i + 1, nodeChild):
                                return True
                    return False
                else:
                    # If it's not a dot.
                    index = ord(char) - ord('a')
                    # If it doesnt exist
                    if currNode.child[index] == None:
                        return False
                    currNode = currNode.child[index]
            return currNode.completed

        return dfs(0, self.root)


        
