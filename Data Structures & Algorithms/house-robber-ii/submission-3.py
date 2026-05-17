class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(dp, numsArray, val):
            if val == 0:
                dp[val] = numsArray[val]
                return dp[val]
            elif val == 1:
                dp[val] = max(numsArray[val], numsArray[val-1])
                return dp[val]
            elif dp[val] != -1:
                return dp[val]
            else:
                dp[val] = max(recurse(dp, numsArray, val-1), 
                                recurse(dp, numsArray, val-2) + numsArray[val])
                return dp[val]
        if len(nums) == 1:
            return nums[0]

        # Will go 0 to lenN - 1
        # Will go 1 to lenN
        firstDp = [-1] * (len(nums) - 1)
        secondDp = [-1] * (len(nums) - 1)
        firstMax = recurse(firstDp, nums[1:], len(nums) - 2)
        secondMax = recurse(secondDp, nums[:len(nums)-1], len(nums) - 2)
        return max(firstMax, secondMax)


