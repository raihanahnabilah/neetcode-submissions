class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) # This is O(nlogn)

        if len(s) != len(t):
            return False

        dictionary = {}

        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        
        for char in t:
            if char not in dictionary or dictionary[char] == 0:
                return False
            else:
                dictionary[char] -= 1
        
        return True
        


