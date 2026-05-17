class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        # time complexity: O(nlogn)
        # space complexity: O(1)
        # return sorted(s) == sorted(t)

        
        # Solution 2
        # time complexity: O(n)
        # space complexity: O(m) -> m is the number of unique characters
        map_s = {}
        map_t = {}

        for char_s in s:
            if char_s in map_s:
                map_s[char_s] += 1
            else:
                map_s[char_s] = 1
        
        for char_t in t:
            if char_t in map_t:
                map_t[char_t] += 1
            else:
                map_t[char_t] = 1
                
        return map_s == map_t

