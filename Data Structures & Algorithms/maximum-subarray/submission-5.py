class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # A better solution with Kadane's algorithm?
        res = float("-inf")
        currVal = 0
        for num in nums:
            currVal += num
            res = max(currVal, res)

            if currVal < 0: # if less than 0, we restart
                currVal = 0 
            

        return res





