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

        res = 0
        def recurse(val):
            nonlocal res

            if val < 0:
                return
            elif val == 0:
                res += 1
            else:
                recurse(val-1)
                recurse(val-2)

        recurse(n)
        return res
            




