class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # non-decreasing order: increasing order
        
        # [1,5,6,7] -> target: 11
        # left: 1, right: 7 -> total: 8
        # if target > total:
        # leftIndex += 1
        # left: 5, right: 7 -> total: 12
        # rightIndex -= 1
        # left: 5, right: 6 -> total: 11

        left, right = 0, len(numbers) - 1
        while left <= right:
            currTotal = numbers[left] + numbers[right]
            if target > currTotal:
                left += 1
            elif target < currTotal:
                right -= 1
            else:
                # print("left", left)
                # print("right", right)
                break
        
        # print("left after", left)
        # print("right after", right)
        return [left + 1, right + 1]
        


            
