# Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # dict to track occurence of numbers
        hashmap = {}
        
        # put string into hashmap
        for letter in s:
            hashmap[letter] = 1 + hashmap.get(letter, 0)
         
        # subtract occurences in second string
        for letter in t:
            hashmap[letter] = hashmap.get(letter, 0) - 1
            
        # return key without 0th value   
        for char in hashmap.keys():
            if hashmap[char] != 0:
                return char