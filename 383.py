# Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # hashmap to store magazine chars
        hm = {}
        
        # map string 
        for char in magazine:
            hm[char] = 1 + hm.get(char, 0)
        
        # check second string
        for char in ransomNote:
            if char in hm and hm[char] > 0:
                hm[char] -= 1
            else:
                return False
            
        return True