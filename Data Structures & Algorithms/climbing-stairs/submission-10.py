class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = [-1] * (n+1)
        def recurse(val):
            # basecase
            if memoize[val] != -1:
                return memoize[val]     
            if val == 0:
                return 1
            if val < 0:
                return 0
            # recursive case
            memoize[val-1] = recurse(val-1)
            memoize[val-2] = recurse(val-2)
            return memoize[val-1] + memoize[val-2]
        
        return recurse(n)
        

