# Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if the two strings are not equal length then they cant be anagrams
        if len(s) != len(t):
            return False
        
        # Using 2 hashmaps to store all values in each string
        hashmapS, hashmapT = {}, {}
          
        for i in range(len(s)):
            
            # increment the character in the hashmaps, or if they arent in the hashmap default             to 0 before incrementing
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        
        for c in hashmapS:

            # for each element, if the char in hashS does not equal the same char using get()             in hashT return False
            if hashmapS[c] != hashmapT.get(c, 0):
                return False
        return True