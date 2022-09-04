# Minimum Deletions to Make Character Frequencies Unique

class Solution:
    def minDeletions(self, s: str) -> int:
        
        # create a hashmap and a set to log values and their counts, as well as unique values
        hashmap = {}
        seen = set()
        counter = 0
        
        # iterate through s and add char to hashmap or increment if already exists
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        # iterate through counts and add count to the unique set of values seen
        for value in hashmap.values():
            while value in seen and value != 0:
                value -= 1
                counter += 1
            seen.add(value)
            
        return counter