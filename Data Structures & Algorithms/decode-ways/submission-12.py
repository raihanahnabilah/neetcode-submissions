class Solution:
    def numDecodings(self, s: str) -> int:
        # time complexity: O(n^2) -> because of string slicing
        # space complexity: O(n^2)

        # to achieve through dp with O(n) time and space complexity, we need to use index
        dp = {}

        def recurse(i: int):
            # base case:
            if i in dp:
                return dp[i]

            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0
            
            # recursive case
            ways = recurse(i+1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += recurse(i+2) 
            
            dp[i] = ways

            return ways
            
        return recurse(0) # give the starting index