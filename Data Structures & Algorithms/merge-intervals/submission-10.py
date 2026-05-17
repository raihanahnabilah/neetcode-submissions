class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # [[1,3],[1,5], [6,7]]
        # prev = [1,3]
        # curr = [1,5]
        # if prev[1] >= curr[0]:
        # prev = min, max, dont insert yet

        # if prev[1] < curr[0]:
        # insert prev
        # curr becomes prev

        # time complexity: O(nlogn) -> due to sorting
        # space complexity: O(n)

        # need to sort: # O(nlogn)
        intervals.sort(key=lambda interval: interval[0])
        
        res = []
        for i, interval in enumerate(intervals):
            if i == 0:
                prev = interval
                continue
            if prev[1] >= interval[0]:
                prev = [min(prev[0], interval[0]), max(prev[1], interval[1])]
            else:
                res.append(prev)
                prev = interval

        res.append(prev)
        return res



                


