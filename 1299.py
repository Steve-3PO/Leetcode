# Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # largest we see at first will be the first index going right to left
        largest = arr[-1]

        # since the last index has no right neighbour it can always be set to -1
        arr[-1] = -1

        # going back from the penultimate element
        for i in range(len(arr) - 2, -1, -1):

            # store the current value and change it to the largest seen
            curr = arr[i]
            arr[i] = largest

            # update the largest we have seen before continuing
            largest = max(curr, largest)
        
        return arr
