# Divisor Game

class Solution:
    def divisorGame(self, n: int) -> bool:

        # playing optimal means both players take x == 1, only depends on whether number is even/odd
        if n % 2 == 0:
            return True
        else:
            return False