# Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # strings must be equal length
        if len(s) != len(t):
            return 0
        
        # remove edge case of empty strings
        if len(s) == 0 and len(t) == 0:
            return 1

        # to track the chars used in string t
        used_values = set()
        
        # to map the relations
        hashmap = {}
        
        
        for i in range(len(s)):
            
            # if s has not been used
            if s[i] not in hashmap:
                
                # if t has been assigned already
                if t[i] in used_values:
                    return False
                
                # assign in the dictionary to each other. Add t to seen set
                hashmap[s[i]] = t[i]
                used_values.add(t[i])
            
            # if s[i] is in hashmap, check if it is the correct char in t
            else: 
                if hashmap[s[i]] != t[i]:
                    return False
            
        return True 