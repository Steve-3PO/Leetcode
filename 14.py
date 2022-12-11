# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # require an output string
        output = ''
        
        # pick a random string in the list, first index is easiest
        for i in range(len(strs[0])):
            
            # compare all other strings to it, if its not long enough or is different return string output
            for s in strs:
                if len(s) <= i or s[i] != strs[0][i]:
                    return output
            
            # after checking all add the char
            output += strs[0][i]
           
        return output