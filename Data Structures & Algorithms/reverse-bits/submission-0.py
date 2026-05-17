class Solution:
    def reverseBits(self, n: int) -> int:
        # using in-built
        binary_rep = bin(n)[2:].zfill(32)

        # reverse it
        # print(binary_rep[::-1])

        return int(binary_rep[::-1], 2)
