# Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:

        # reverse the binary value of integer, drop the last 2 values as they are 0b (data type)
        reversed = bin(n)[::-1][:-2]

        # add the zeros that were removed during conversion
        reversed = reversed + '0'*(32 - len(reversed))

        # return as integer
        return int(reversed, 2)