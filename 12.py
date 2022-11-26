# Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        # must create a list of all possible unique values, which will be interated over each to see how many exist within num
        symbols = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        
        # string to append results to
        string = ""
        
        # iterate through each pair
        for pair in symbols:
            
            # the occurances of a number is the floor 
            multiplier = num // pair[1]
            
            # add the occurances * symbol to the string
            string = string + (multiplier * pair[0])
            
            # modulus will subtract if neccessary
            num = num % pair[1]
        return string