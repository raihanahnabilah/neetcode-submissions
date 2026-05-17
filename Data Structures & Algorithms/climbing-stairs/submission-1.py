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


        res = 0

        def recurse(n):
            nonlocal res
            
            if n == 0:
                res += 1
                return
            if n < 0:
                return
            recurse(n-1)
            recurse(n-2)
        
        recurse(n)

        return res

        