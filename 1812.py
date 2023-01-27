# Determine Color of a Chessboard Square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        # create hashmap to break up even values into white vs black
        evenwhite = {'a':'a', 'c':'c', 'e':'e', 'g':'g'}

        # check if tile is even number
        if int(coordinates[1]) % 2 == 0:

            # if even, and in hashmap we know it must be white
            if coordinates[0] in evenwhite:
                return True

            # otherwise its a black tile
            else:
                return False
        
        # if its not an even number, check if its hashmap, if it is it must be black tile
        else:
            if coordinates[0] in evenwhite:
                return False

            # otherwise its a white tile 
            else:
                return True