class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # [[1,3], [4,6]]
        # [2,5]
        
        # 1.  3
        #.  2.  5 
        # for it to not overlap, then 5 < 1

        # 1,2
        # newInterval = [5,6]
        # 1 2
        #.    5 6 
        # newInterval[1] < interval[0]: we wanna insert the newInterval + intervals[i:]
        # if the new interval is at the end:
        # interval[1] < newInterval[0]: we wanna insert interval
        # else, they overlap!

        # intervals are sorted!
        intervals.sort(key=lambda interval: interval[0])
        
        res = []
        for i, currInterval in enumerate(intervals):
            if newInterval[1] < currInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif currInterval[1] < newInterval[0]:
                res.append(currInterval)
            else:
                newInterval = [min(newInterval[0], currInterval[0]), max(newInterval[1], currInterval[1])]
        
        res.append(newInterval)
        return res







