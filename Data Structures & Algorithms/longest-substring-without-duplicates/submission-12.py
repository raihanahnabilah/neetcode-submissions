class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        res = 1
        left_pointer = 0
        right_pointer = 1

        curr_set = set()
        curr_set.add(s[left_pointer])
        while left_pointer <= right_pointer and left_pointer < len(s) and right_pointer < len(s):
            if s[right_pointer] in curr_set:
                while s[right_pointer] in curr_set:
                    curr_set.remove(s[left_pointer])
                    left_pointer += 1
            curr_set.add(s[right_pointer])
            res = max(res, right_pointer - left_pointer + 1)
            right_pointer += 1

        return res






            
        