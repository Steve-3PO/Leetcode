# Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        # first initialise cows
        bull, cow = 0, 0
             
        # now we need 2 substitute lists of secret and guess it modify
        s = list(secret)
        g = list(guess)
                
        # now require two variables to iterate
        i, j = 0, 0
        
        # iterate through length of guess
        while i < len(guess):
        
            # if there is a match, increment bull and remove element
            if s[j] == g[j]:
                bull += 1
                s.pop(j)
                g.pop(j)
                
            # otherwise move along   
            else:
                j += 1
            i += 1  
            
        # create a counter for the word substitute
        count = Counter(s) 
        
        # if the char is in the table of count and occurence is greater than 0, decrement           occurence and increase cow
        for l in g:
            if l in count and count[l] > 0:
                cow += 1
                count[l] -= 1
                
        return "{}A{}B".format(bull, cow)