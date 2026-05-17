class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        
        if len(intervals) < 2:
            return res

        # need to sort it -> but apparently we need to sort it by the second value
        intervals.sort(key=lambda array: array[1]) #sort by second value

        prevInterval = intervals[0]
        for currInterval in intervals[1:]:
            if prevInterval[1] <= currInterval[0]:
                # print("prev curr", prevInterval, currInterval)
                prevInterval = currInterval
            else:
                # means this overlaps
                res += 1
            
        return res
