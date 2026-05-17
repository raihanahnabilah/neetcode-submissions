class Node:
    def __init__(self):
        self.child = [None] * 26
        self.completed = False

class PrefixTree:
    def __init__(self):
        self.rootNode = Node()

    def insert(self, word: str) -> None:
        currNode = self.rootNode
        for char in word:
            # print("Checking char and numChar and completed after", char, currNode.completed)
            numChar = ord(char) - ord('a')
            if currNode.child[numChar] == None:
                newNode = Node()
                currNode.child[numChar] = newNode
            currNode = currNode.child[numChar]
            # print("Checking char and numChar and completed before", char, currNode.completed)
        currNode.completed = True


    def search(self, word: str) -> bool:
        currNode = self.rootNode
        for char in word:
            numChar = ord(char) - ord('a')
            if currNode.child[numChar] == None:
                return False
            currNode = currNode.child[numChar]
        return currNode.completed

    def startsWith(self, prefix: str) -> bool:
        currNode = self.rootNode
        for char in prefix:
            numChar = ord(char) - ord('a')
            if currNode.child[numChar] == None:
                return False
            currNode = currNode.child[numChar]
        return True
        