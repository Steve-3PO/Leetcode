# Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # i starts from last index
        i = -1
        
        # boolean to know if we are on the last word, and length to increment
        lastwordfound = False
        length = 0
        
        # for the length of s keep iterating
        while -i <= len(s):
            
            # when space is found, if we have found the last word it must be the end of the string, otherwise it will be a space at the end of the input s
            if s[i] is " ":
                if lastwordfound == True:
                    return length
            
            # check if each char isalpha, if it is increment length and set boolean = True
            elif s[i].isalpha() == True:
                lastwordfound = True
                length += 1
            
            i -= 1
        
        return length