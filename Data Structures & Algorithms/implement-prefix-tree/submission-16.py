class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    # time complexity: O(n) for each call
    # space complexity: O(t) -> total number of TrieNodes
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        trie_node = self.root
        for char in word:
            if char not in trie_node.children:
                trie_node.children[char] = TrieNode()
            trie_node = trie_node.children[char]
        trie_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        trie_node = self.root   
        for char in word:
            if char not in trie_node.children:
                return False
            trie_node = trie_node.children[char]
        return trie_node.is_end_of_word        

    def startsWith(self, prefix: str) -> bool:
        trie_node = self.root   
        for char in prefix:
            if char not in trie_node.children:
                return False
            trie_node = trie_node.children[char]
        return True



        