class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.descendingArray = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        # Brute force
        self.descendingArray.append(val)
        self.descendingArray = sorted(self.descendingArray, reverse=True)
        return self.descendingArray[self.k-1]
        

# top -> kth largest element
# stack = [3,3,2,1]

# append it!
# sort it again
# get the kth one




