"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True

        # sort it -> O(nlogn)
        intervals.sort(key= lambda interval: interval.start)        

        prevInterval = intervals[0]
        # non overlapping if:
        for i in range(1, len(intervals)):
            if prevInterval.end > intervals[i].start:
                return False
            prevInterval = intervals[i]
        
        return True