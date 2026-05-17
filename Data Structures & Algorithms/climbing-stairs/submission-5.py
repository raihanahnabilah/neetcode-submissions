class Solution:
    def climbStairs(self, n: int) -> int:
        counter = 0

        def recursion(num: int):
            if num == 0:
                nonlocal counter
                counter += 1
                return
            
            if num < 0:
                return
            
            recursion(num-1)
            recursion(num-2)
        
        recursion(n)

        return counter
