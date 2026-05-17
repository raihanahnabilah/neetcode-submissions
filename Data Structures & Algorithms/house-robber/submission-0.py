class Solution:
    def rob(self, nums: List[int]) -> int:
        # Cannot use odd and even
        # Just cannot rob two adjacent houses

        # 1,1,3,3
        # 1 -> max = 1
        # 1,1 -> max = 1
        # 1,(1+3) -> max = 4
        # 4, (1+3) - > max = 4

        dp = [-1] * len(nums)

        def recurse(currHouse):
            if currHouse == 0:
                dp[currHouse] = nums[currHouse]
                return dp[currHouse]
            elif currHouse == 1:
                dp[currHouse] = max(nums[currHouse - 1], nums[currHouse])
                return dp[currHouse]
            elif dp[currHouse] != -1:
                return dp[currHouse]
            else:
                dp[currHouse] = max(recurse(currHouse - 1), 
                                    recurse(currHouse - 2) + nums[currHouse])
                return dp[currHouse]

        return recurse(len(nums) - 1)

        




