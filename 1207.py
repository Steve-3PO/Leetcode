# Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # require a hashmap where we will track occurences of each value
        hashmap = {}

        # iterate through array and increment in the dictionary the corresponding value count
        for val in arr:
            hashmap[val] = 1 + hashmap.get(val, 0)

        # can use a set to track unique occurences
        seen = set()

        # check if each occurence is unique using set, if not return false
        for val in hashmap.values():
            if val not in seen:
                seen.add(val)
            else:
                return False

        return True