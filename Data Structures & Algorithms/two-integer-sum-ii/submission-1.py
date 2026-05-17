class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order - increasing order

        # Solution 1 -> regular two sum
        # This is O(n)
        # But this doesnt take advantage of the increasing order
        # num_to_index = {}
        # for i, num in enumerate(numbers):
        #     if (target-num) in num_to_index and num_to_index[target-num] < i + 1:
        #         return [num_to_index[target-num], i + 1]
        #     else:
        #         num_to_index[num] = i + 1


        # Solution 2 -> two pointers
        leftPointer = 0
        rightPointer = len(numbers) - 1

        while leftPointer < rightPointer:
            if target == numbers[leftPointer] + numbers[rightPointer]:
                return [leftPointer + 1, rightPointer + 1]
            elif target < numbers[leftPointer] + numbers[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
            


