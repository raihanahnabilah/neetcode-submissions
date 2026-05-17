class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = []
        for num in range(0,n+1):
            output.append(bin(num).count('1'))        
        return output

        