# Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        i = 1
        while i <= len(s):
            if s[i] == s[i - 1]:
                s.replace(s[i - 1], "")
                s.replace(s[i - 1], "")
            elif s[i] == s[i + 1]:
                s.replace(s[i], "")
                s.replace(s[i], "")
            else:
                i += 1

        
        return s