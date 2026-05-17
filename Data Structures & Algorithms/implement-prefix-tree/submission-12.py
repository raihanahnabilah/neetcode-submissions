class Node:
    def __init__(self):
        self.children = [None] * 26
        self.completed = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not currNode.children[index]:
                newNode = Node()
                currNode.children[index] = newNode
            currNode = currNode.children[index]
        currNode.completed = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            currNode = currNode.children[index]
            print(char, currNode.completed)
            if not currNode:
                return False
        return currNode.completed

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            currNode = currNode.children[index]
            if not currNode:
                return False
        return True


        
        