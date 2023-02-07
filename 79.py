# Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # initialise rows and column variables
        ROWS, COLS = len(board), len(board[0])

        # we require a set to know which indexes we have used
        path = set()

        # using dfs function
        def search(r, c, i):

            # when i is larger than the length of the word - 1, it must have found it
            if i == len(word):
                return True
            
            # no result when r or c are out of bounds, or if chars dont match or index has been used
            if ((r < 0 or c < 0) or (r >= ROWS or c >= COLS) or board[r][c] != word[i] or (r, c) in path):
                return False

            # add the index to the set
            path.add((r, c))

            # conduct new searches
            res = (
                search(r + 1, c, i + 1)
                or search(r - 1, c, i + 1)
                or search(r, c + 1, i + 1)
                or search(r, c - 1, i + 1)
            )

            # remove the current index
            path.remove((r, c))

            # return the new dfs, which would have already run, essentially only returning back true or false
            return res

        # go through each index as starting and see which complete
        for r in range(ROWS):
            for c in range(COLS):
                if search(r, c, 0):
                    return True
        return False
            
            
            
            
            

            