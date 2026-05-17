class Solution:
    def reverseBits(self, n: int) -> int:
        # # using in-built
        # binary_rep = bin(n)[2:].zfill(32)

        # # reverse it
        # # print(binary_rep[::-1])

        # return int(binary_rep[::-1], 2)


        # Brute force but not using in built
        binary_rep = ""
        for i in range(32):
            if n & (1 << i): # shift the bit by 1 and i to add 1
                binary_rep += "1"
            else:
                binary_rep += "0"
        
        res = 0
        # now to convert the binary_rep reversed to a number
        for i, bit in enumerate(binary_rep[::-1]):
            # we only care when the bit is 1
            if bit == "1":
                res |= (1 << i)# we wanna OR that to the number

        return res
