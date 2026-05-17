class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # def validPalindrome(cleaned):
        #     left = 0
        #     right = len(cleaned) - 1

        #     while left <= right:
        #         if cleaned[left] != cleaned[right]:
        #             return False
        #         left += 1
        #         right -= 1
            
        #     return True
    
        # # pkkwka
        # # p, k, k, w, k, a
        # # kk
        # # kwk
        # # 8

        # # Brute force:
        # # To try every single combination through
        # # nested for loop
        # # And then check through validPalindrome?
        # res = len(s)

        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if j <= i:
        #             continue
        #         else:
        #             isPalindrome = validPalindrome(s[i:j+1])
        #             res = res + (1 if isPalindrome else 0)

        # return res

        res = 0

        for i in range(len(s)):
            # odd length
            left = right = i
            while left <= right and left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # even length
            left = i
            right = i + 1
            while left <= right and left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1    

        return res


