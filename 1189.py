# Maximum Number of Balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # need a hashmap to track letter occurence
        hashmap = {"b":0 , "a":0 , "l":0 , "o":0 , "n":0}

        # looking at each char
        for char in text:

            # convert to lower to fit hashmap and check if it is a letter within the wanted string
            if char.lower() in hashmap:
                
                # sine l and o appear twice we need twice the ammount so we only add half a value each time
                if char == "l" or char == "o":
                    hashmap[char] += 0.5
                
                # other letters do not appear twice
                else:
                    hashmap[char] += 1

        # find the floor of the minimum and that is the bottleneck for how many words we can make 
        minimum = 10**4
        for val in hashmap.values():
            minimum = min(minimum, floor(val))

        return minimum