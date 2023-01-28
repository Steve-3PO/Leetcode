# Distribute Candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # Alice can either eat all unique candies if the no. of unique candies < how many she can eat, otherwise she can only eat the amount of unique candies she is allowed (always pick the minimum as the bottleneck)

        # number of candies shes allowed
        length1 = len(candyType) / 2

        # number of unique candies
        seen = set()
        unique = 0
        for val in candyType:
            if val not in seen:
                unique += 1
                seen.add(val)
        
        # if shes allowed more than there are unique, she can have them all, otherwise she can only have what she is allowed
        return int(min(unique, length1))
            

