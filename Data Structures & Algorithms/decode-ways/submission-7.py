class Solution:
    # iterative dp
    # time complexity: O(n + 1)
    # space complexity: O(n)
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        next1 = 1
        next2 = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else: 
                curr = next1
                if 10 <= int(s[i:i+2]) <= 26 and i+2 <= len(s):
                    curr += next2
            
            next2 = next1
            next1 = curr

        return next1