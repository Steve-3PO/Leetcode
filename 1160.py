# Find Words That Can Be Formed by Characters

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        # since all strings only use lower case alphabet we can use ascii values in a string to map
        charmap = [0] * 26

        # total to track length added
        total = 0

        # map characters to a list, each index represents ascii value (List[0] == a, List[1] == b)
        for char in chars:
            charmap[ord(char) - 97] += 1

        # iterate through each word
        for word in words:
            
            # from a blank list, and assume word is ok to add (in case string is empty it defaults to True)
            curr = [0] * 26
            word_ok = True

            # for each character in the seected word
            for letter in word:

                # if the character is present in the original word map and is greater than the occurence in the current word map, we can add 1 to current map and continue.
                if curr[ord(letter) - 97] < charmap[ord(letter) - 97]:
                    curr[ord(letter) - 97] += 1

                # if word occurs more times than is seen in char map, word cannot be made
                else:
                    word_ok = False
                    break
                    
            # checks for word to be added
            if word_ok == True:
                total += len(word)

        return total
        
