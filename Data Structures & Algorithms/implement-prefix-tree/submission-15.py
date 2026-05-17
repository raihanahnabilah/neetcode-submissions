class TreeNode:
    def __init__(self, end_of_the_word = False):
        self.children = {}
        self.end_of_the_word = end_of_the_word



class PrefixTree:

    def __init__(self):
        self.root = TreeNode() 

    def insert(self, word: str) -> None:
        curr_children = self.root.children
        for i, char in enumerate(word):
            if char not in curr_children:
                if i == len(word) - 1:
                    curr_children[char] = TreeNode(True)
                else:
                    curr_children[char] = TreeNode() 
            else:
                if i == len(word) - 1:
                    curr_children[char].end_of_the_word = True                 
            curr_children = curr_children[char].children
            
    def search(self, word: str) -> bool:
        curr_children = self.root.children
        for i, char in enumerate(word):
            if char not in curr_children:
                return False
            else:
                if i == len(word) - 1:
                    curr_children = curr_children[char]
                else:
                    curr_children = curr_children[char].children

        return curr_children.end_of_the_word

    def startsWith(self, prefix: str) -> bool:
        curr_children = self.root.children
        for i, char in enumerate(prefix):
            if char not in curr_children:
                return False
            else:
                curr_children = curr_children[char].children

        return True



        