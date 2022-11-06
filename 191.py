class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # initiate a count for all 1 occurences
        count = 0
        
        while n:
            
            # modulo will always tell 1/0 in the first index position
            count += n % 2
            
            # then we interate until every index is checked
            n = n >> 1
            
        return count