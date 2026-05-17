class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time complexity: O(n)
        # space complexity: O(1)
        
        heapq.heapify(nums) # O(n)
        while len(nums) > k:
            heapq.heappop(nums) # O(logn)
        return nums[0]
