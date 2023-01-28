# Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        # split setence into list
        s = s.split()

        # return the first k elements joined with a space
        return " ".join(s[:k])