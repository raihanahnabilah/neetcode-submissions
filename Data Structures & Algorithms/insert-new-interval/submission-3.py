class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # Ensuring the overlapping intervals is to ensure that it's not before or after the interval
    # hence we check if interval[0] is NOT larger than newInterval[1] and 
    # interval[1] is NOT smaller than newInterval[0]

    # e.g. [[1,3], [4,6]]
    # newInterval = [2,5]

        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                # wanna check for overalp?
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        
        return res


