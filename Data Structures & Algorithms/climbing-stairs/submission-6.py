class Solution:
    def climbStairs(self, n: int) -> int:
        # Method 1:
        # Time complexity: O(2^n)
        # Space complexity: O(n)
        # counter = 0

        # def recursion(num: int):
        #     if num == 0:
        #         nonlocal counter
        #         counter += 1
        #         return
            
        #     if num < 0:
        #         return
            
        #     recursion(num-1)
        #     recursion(num-2)
        
        # recursion(n)

        # return counter

        # Method 2: Dynamic programming
        cached = [-1] * (n+1)
        def dfs(num):
            if cached[num] != -1:
                return cached[num]
            
            if num == 0:
                return 1
            
            if num < 0:
                return 0

            cached[num-1] = dfs(num-1)
            cached[num-2] = dfs(num-2)
            return cached[num-1] + cached[num-2]

        return dfs(n)







