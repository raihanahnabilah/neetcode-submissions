class Solution:
    def countBits(self, n: int) -> List[int]:
        # convert to binary representation
        res = []

        for i in range(n+1):
            i_binary = bin(i)[2:]
            ones_counter = 0
            for ibin in i_binary:
                if ibin == "1":
                    ones_counter += 1
            res.append(ones_counter)
        return res
