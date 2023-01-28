# Count Largest Group

class Solution:
    def countLargestGroup(self, n: int) -> int:

        # will use a hashmap to track the groups and their occurences
        hashmap = {}

        # iterating through each num
        for val in range(1, n + 1):

            # find the sum of its digits
            total = 0
            for char in str(val):
                total += int(char)
            
            # add it to the hashmap if not exist, otherwise increment group count for that total
            hashmap[total] = 1 + hashmap.get(total, 0)
        
        res = 0
        maximum = 0

        # going through each group, if its the new largest set result to 1, otherwise we increment if its the same
        for count in hashmap.values():
            if count > maximum:
                maximum = count
                res = 1
            elif count == maximum:
                res += 1
            

        return res