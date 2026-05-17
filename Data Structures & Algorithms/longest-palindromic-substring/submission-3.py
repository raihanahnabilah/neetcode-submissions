class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # print("Checking i", i)
            left = i
            right = i
            while left <= right and left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    # print("checking s[left]", s[left], s[right], len(res), left, right)
                    if right - left + 1 > len(res):
                        res = s[left:right+1]
                        # print("checking res", res)
                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i + 1
            while left <= right and left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if right - left + 1 > len(res):
                        res = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
        return res
          

