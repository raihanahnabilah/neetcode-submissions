class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nested for loop
        # O(n^2) -> see every subarray there is
        # sliding window?
        # 2, 2 + -3 = -1
        # 2

        # 0,1 = -1
        # 1,2 = 1
        # 2,3 = 2
        # 3,4 = 0
        # 4,5 = 3
        # 5,6 = 0
        # 6,7 = 3


        res = float("-inf")
        currentMax = 0

        for num in nums:
            if currentMax < 0:
                currentMax = 0
            
            currentMax += num
            res = max(res, currentMax)

        return res


