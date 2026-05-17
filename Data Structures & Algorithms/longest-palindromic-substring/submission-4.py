class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_left = 0
        res_right = 0
        for i, char in enumerate(s):

            # for odd             
            left = right = i
            while left <= right and left >= 0 and right < len(s) and s[left] == s[right]:           
                curr_res = (right-left) + 1
                if curr_res > res:
                    res_left = left
                    res_right = right
                    res = curr_res
                left -= 1
                right += 1
            
            # for even
            left = i
            right = i + 1
            while left <= right and left >= 0 and right < len(s) and s[left] == s[right]:           
                curr_res = (right-left) + 1
                if curr_res > res:
                    res_left = left
                    res_right = right
                    res = curr_res
                left -= 1
                right += 1
            
        return s[res_left:res_right+1]

