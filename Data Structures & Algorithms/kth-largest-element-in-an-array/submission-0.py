class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution 1 - with sorting
        nums.sort(reverse = True)
        return nums[k-1]