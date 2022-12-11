# Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # check if n is 0 edgecase
        if n == 0:
            return True

        # iterate through each position
        for i in range(len(flowerbed)):

            # when an empty space is found
            if flowerbed[i] == 0:

                # determine true if either statements are true
                leftside = (i == 0) or (flowerbed[i - 1] == 0)
                rightside = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # if both are true then you can insert a flower
                if leftside and rightside:
                    flowerbed[i] = 1
                    n -= 1
                    
                    # check if done
                    if n == 0:
                        return True

        return False
        
               