class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # Solution 1 - with sorting
        # # Time complexity: O(nlogn)
        # # Space complexity: O(n)
        # nums.sort(reverse = True)
        # return nums[k-1]

        # # Solution 2 - with heap
        # # Time complexity: O(logk)
        # # Space complexity: O(k)
        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        # return nums[0]

        # Solution 3 - with array
        minVal = min(nums)
        maxVal = max(nums)
        arrayChecker = [0] * (maxVal - minVal + 1)

        for num in nums:
            arrayChecker[num - minVal] += 1
        
        # [2,1,1,1,2]
        res = 0
        for i in range(len(arrayChecker)-1, -1, -1):
            res += arrayChecker[i]
            if res >= k:
                return i + minVal



