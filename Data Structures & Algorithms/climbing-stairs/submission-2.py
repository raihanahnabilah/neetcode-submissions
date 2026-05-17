class Solution:
    def climbStairs(self, n: int) -> int:

        # res = 0

        # def recurse(n):
        #     nonlocal res

        #     if n == 0:
        #         res += 1
        #         return
        #     if n < 0:
        #         return
        #     recurse(n-1)
        #     recurse(n-2)
        
        # recurse(n)

        # return res

        cache = [-1] * n

        def recurse(n):            
            if n == 0:
                return 1
            if n < 0:
                return 0
            print("checking", cache[n-1])
            if cache[n-1] == -1:
                cache[n-1] = recurse(n-1) + recurse(n-2)
            
            return cache[n-1]

        return recurse(n)

        