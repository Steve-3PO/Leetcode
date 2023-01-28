# Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # a pointer either end of the string
        l = 0
        r = len(s) - 1

        # turn string into list
        s = list(s)

        # while pointers have not crossed
        while l < r:

            # find the alphabetic chars
            while not s[l].isalpha() and l < r:
                l += 1
            while not s[r].isalpha() and l < r:
                r -= 1

            # swap them around
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            # keep integrating
            l += 1
            r -= 1
        
        # turn list back to a string
        return "".join(s)