class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First need to sort this
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1 # left
            k = len(nums) - 1 #right
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]]) 
                    j += 1 
                    # Traverse more and to avoid duplicates
                    while k > j and nums[j] == nums[j-1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return res



