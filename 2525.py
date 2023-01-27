# Categorize Box According to Criteria

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        # since only 2 vaiables to track we can use a short list with true false values
        bulkyheavy = [0, 0]

        # check if values should be true or false depending on parameters
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or (length * width * height) >= 10**9:
            bulkyheavy[0] = 1
        if mass >= 100:
            bulkyheavy[1] = 1
        
        # determine what should be returned
        if bulkyheavy == [0, 0]:
            return "Neither"
        elif bulkyheavy == [1, 1]:
            return "Both"
        elif bulkyheavy == [1, 0]:
            return "Bulky"
        else:
            return "Heavy"