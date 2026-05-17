class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 2
        # 1 + 1
        # 2

        #   3
        # 2.   1
        #1. 0.0 
        #0 

        # Base case: 
        # if == 0: res += 1
        # if < 0: return 
        # Recursive case:
        # recurse(-1)
        # recurse(-2)
        dp = [-1] * (n + 1)
        def recurse(val):

            if val < 0:
                return 0
            elif dp[val] != -1:
                return dp[val]
            elif val == 0:
                return 1
            else:
                return recurse(val-1) + recurse(val-2)

        return recurse(n)

        #.    2
        #. 1.   0
        # 0.   

        #      3 
        #  2.     1
        # 1 0       0
        # 0
            




