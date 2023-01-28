# Replace All Digits with Characters

class Solution:
    def replaceDigits(self, s: str) -> str:

        # turn s into a list so we can assign values in place
        s = list(s)

        # iterating through each element in s
        for i in range(len(s)):

            # when an element is alphabetic, we want to remember the char incase the next value is a number
            if s[i].isalpha():
                prev = s[i]

            # when we come across a number we then increase the prev element by the new ascii value
            else:
                new = ord(prev) + int(s[i])
                s[i] = chr(new)
        
        # join the list back together
        return "".join(s)