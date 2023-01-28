# Goat Latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        # create string variable which will be added to
        res = ""

        # set of vowels to determine which operation to use
        dic = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        # split sentence into list of words
        sentence = sentence.split(" ")

        # iterate through each word, tracking the index to append 'a's to the end of each word
        for index, word in enumerate(sentence):

            # word beginning with a vowel
            if word[0] in dic:
                res += word + "ma" 
            
            # consonant words
            else:
                res += word[1:] + word[0] + "ma"

            # adding additional 'a's depending on index
            res += "a" * (index + 1)
            res += " "
        
        # remember there is an extra space at the end
        return res[:-1]
