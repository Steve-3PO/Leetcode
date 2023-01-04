# Circular Sentence

class Solution:
    def isCircularSentence(self, s: str) -> bool:

        # return true if the first and last chars are the same, as well as all beginning and ending chars between words
        # must use s.split to create a list of strings, and all() to create a boolean from a generator
        return True if ((ws:=s.split(' '))[0][0] == ws[-1][-1]) and all(ws[i][-1] == ws[i + 1][0] for i in range(len(ws)-1)) else False