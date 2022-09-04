# Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # to make a palindrome we only care about all the even number occurance
        # of letters and largest odd number occurance. The rest of the odds
        # we subtract 1 from and add as even numbers
        
        # we need a dict as we must track the letter and its occurance 
        hashmap = {}
        
        # iterating through string s, if its not in hashmap, we add
        # if it is then we increment by 1
        for c in range(len(s)): 
            if s[c] not in hashmap:
                hashmap[s[c]] = 1
            else:
                hashmap[s[c]] += 1
                
        # create a running sum and a boolean to track if we have seen an odd 
        # number yet
        total = 0
        seenodd = False
        
        # interating through each occurance in hashmap, if it is odd and we have
        # already come across an odd number then we add the value minus 1 to make 
        # it even
        for key, val in hashmap.items():
            if val % 2:
                if seenodd:
                    total += val - 1
                    
                # if we havent seen an odd occurance yet, we change the boolean
                # and add the odd number 
                else:
                    seenodd = True
                    total += val
                
            # in the case of even numbers we just add to total
            else:
                total += val
        return total