# Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # create 2 lists to pop from
        S_out = []
        t_out = []
        
        # append each s char or pop if #
        for char in s:
            if char == "#":
                if len(S_out) > 0: S_out.pop()
            else:
                S_out.append(char)
        
        # append each t char or pop if #
        for char in t:
            if char == "#":
                if len(t_out) > 0: t_out.pop()
            else:
                t_out.append(char)
        
        return S_out == t_out