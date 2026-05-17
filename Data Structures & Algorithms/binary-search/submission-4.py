class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary search works like this:
        # You split array of numbers into two
        # You either go to the left or right
        # Same as if youre looking into a telephone book

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1
