class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        # To have a map
        # Storing the total number of values each time
        # result_s = {}
        # for char_s in s:
        #     if char_s not in result_s:
        #         result_s[char_s] = 1
        #     else:
        #         result_s[char_s] += 1
        
        # result_t = {}

        # for char_t in s:
        #     if char_t not in result_t:
        #         result_t[char_t] = 1
        #     else:
        #         result_t[char_t] += 1
        
        # return result_s == result_t

        
        # Solution 2
        # We sort the string and see if they're equal? 
        # The sorted function is O(nlogn)
        return "".join(sorted(s)) == "".join(sorted(t))
