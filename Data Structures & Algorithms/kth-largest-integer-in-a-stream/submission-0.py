class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    # Brute force solution, sort each time a value is added
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True) # O(nlogn)
        return self.nums[self.k - 1]


        
