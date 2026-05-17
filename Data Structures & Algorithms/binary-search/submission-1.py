class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # divide and conquer
        # will take the middle value -> 
        # if middle value < target -> then go to the middle of left one
        # if middle value > target -> then go to the middle of right one
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left + right) // 2
            if nums[left] == target:
                print("here", left)
                return left
            if nums[right] == target: 
                return right
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1

        return -1