class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order - increasing order

        # Solution 1 -> regular two sum
        num_to_index = {}
        for i, num in enumerate(numbers):
            if (target-num) in num_to_index and num_to_index[target-num] < i + 1:
                return [num_to_index[target-num], i + 1]
            else:
                num_to_index[num] = i + 1


        # Solution 2 -> two pointers

