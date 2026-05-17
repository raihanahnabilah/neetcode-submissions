class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []

        # assumption intervals are sorted?
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        
        if len(intervals) < 2:
            return intervals

        prevInterval = sorted_intervals[0]
        for interval in sorted_intervals:
            currInterval = interval
            # check for overlap
            if prevInterval[1] >= currInterval[0]:
                newInterval = [min(prevInterval[0], currInterval[0]), max(prevInterval[1], currInterval[1])]
                prevInterval = newInterval
            # No overlap
            else:
                res.append(prevInterval)
                prevInterval = currInterval
        
        res.append(prevInterval)

        return res

