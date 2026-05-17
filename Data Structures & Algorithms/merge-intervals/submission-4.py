class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Need to sort the first chars first
        intervals.sort(key = lambda x: x[0])
        
        print(intervals)

        res = [intervals[0]]


        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]

            # Case 1: - curr is not overlapping with previous
            # if prev[1] < curr[0]
            # just append curr
            if prev[1] < curr[0]:
                res.append(curr)

            # Case 2: - curr is overlapping
            # if prev[1] > curr[0]
            else:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                res[-1] = prev

        return res

