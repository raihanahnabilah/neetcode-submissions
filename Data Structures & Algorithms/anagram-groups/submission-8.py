class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # method 1:
        # a bit brute force:
        # sort each word, and put it in a map
        # time complexity: O(m*nlogn)
        # space complexity: O(m*n)

        # map_set_to_strings = {}
        # for word in strs: # O(n)
        #     sorted_word = "".join(sorted(word)) # O(nlogn)
        #     if sorted_word in map_set_to_strings:
        #         map_set_to_strings[sorted_word].append(word)
        #     else:
        #         map_set_to_strings[sorted_word] = [word]
        
        # return list(map_set_to_strings.values())

        # solution 2
        # time complexity: O(m*n)
        # space complexity: O(m*n)
        map_charcount_to_string = {}

        for word in strs: # O(m*n)
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            if tuple(char_count) in map_charcount_to_string:
                map_charcount_to_string[tuple(char_count)].append(word)
            else:
                map_charcount_to_string[tuple(char_count)] = [word]

        return list(map_charcount_to_string.values())