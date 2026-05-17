class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3], [1,5], [6,7]]
        # [1, 3]

        # sort by first value
        intervals.sort(key=lambda x: x[0])

        # 1  3
        # 1.   5
        #.  2. 5

        # if interval[0] <= prevInterval[1]

        res = []

        prevInterval = intervals[0]
        for i in range(len(intervals)):
            if i == 0:
                continue
            
            currInterval = intervals[i]
            if currInterval[0] <= prevInterval[1]:
                prevInterval = [min(currInterval[0], prevInterval[0]), max(currInterval[1], prevInterval[1])]
            else:
                res.append(prevInterval)
                prevInterval = currInterval
        
        res.append(prevInterval)

        return res







        
