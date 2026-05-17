class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # Solution 1 - with sorting
        # nums.sort(reverse = True)
        # return nums[k-1]

        # Solution 2 - with heap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]