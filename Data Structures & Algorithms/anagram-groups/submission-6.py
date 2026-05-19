class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # method 1:
        # a bit brute force:
        # sort each word, and put it in a map
        # time complexity: O(n^2logn)
        # space complexity: O(n)

        map_set_to_strings = {}
        for word in strs: # O(n)
            sorted_word = "".join(sorted(word)) # O(nlogn)
            if sorted_word in map_set_to_strings:
                map_set_to_strings[sorted_word].append(word)
            else:
                map_set_to_strings[sorted_word] = [word]
        
        return list(map_set_to_strings.values())


