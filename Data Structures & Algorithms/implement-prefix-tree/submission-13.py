class TreeNode:
    def __init__(self, end_of_the_word = False):
        self.children = {}
        self.end_of_the_word = end_of_the_word

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        currChildren = self.root.children
        # print("checking currChildren", currChildren)
        for i, char in enumerate(word):
            # print("checking char", char, currChildren)
            if char not in currChildren:
                newNode = TreeNode(False if i != len(word)-1 else True)
                currChildren[char] = newNode
            if i == len(word) - 1:
                currChildren[char].end_of_the_word = True
            currChildren = currChildren[char].children

    def search(self, word: str) -> bool:
        currChildren = self.root.children
        for i, char in enumerate(word):
            if char in currChildren:
                if i == len(word) - 1:                
                    currChildren = currChildren[char]
                else:
                    currChildren = currChildren[char].children
            else:
                return False
        
        return currChildren.end_of_the_word == True

    def startsWith(self, prefix: str) -> bool:
        currChildren = self.root.children
        for char in prefix:
            if char in currChildren:
                currChildren = currChildren[char].children
            else:
                return False
        
        return True
        



        