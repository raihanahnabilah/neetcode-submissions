class Solution:
    def numDecodings(self, s: str) -> int:
        
        def recurse(d: str):
            # base case:
            if len(d) == 0:
                return 1
            
            if d[0] == "0":
                return 0

            # recursive case
            ways = recurse(d[1:])

            if len(d) >= 2 and 10 <= int(d[:2]) <= 26:
                ways += recurse(d[2:])
            
            return ways

        return recurse(s)