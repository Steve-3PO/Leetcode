# Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # cant have s1 permutations in s2 if s1 > s2
        if len(s1) > len(s2):
            return False

        # create two arrays that represent the occurance of each letter, as we know its bound by lowercase         English alphabet
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # iterate through each string and count occurance of each letter
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
               
        # to know if the arrays are equal we need a variable to determine how many out of the 26                 characters are equivalent
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # starting with left pointer on s[0] and right pointer moving from len(s1) to len(s2)
        l = 0
        for r in range(len(s1), len(s2)):
            
            # if matches are all correct, return true
            if matches == 26:
                return True
            
            # if not correct take the ascii value of the element in s2 and add it to the array
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            
            # check if the values are now equivalent, if they are increment matches/otherwise decrement
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # repeat this for the left pointer, taking away from the array
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                
            # increment left pointer
            l += 1
            
        # return true if matches == 26
        return matches == 26