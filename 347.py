# Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a dictionary to track the numbers and their occurence
        dic = {}
        
        # create a freq array to group numbers occurence
        freq = [[] for i in range(len(nums) + 1)]
        
        # for each number, add to dictionary and increment counter
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        
        # for each counter add to frequency with corresponding number
        for n, c in dic.items():
            freq[c].append(n)
            
        # result array to append   
        res = []
            
        # in reverse down the freq array    
        for i in range(len(freq) -1, 0, -1):
            
            # for each element occuring the same number of times
            for n in freq[i]:
                
                # append and stop if k elements are in res array
                res.append(n)
                if len(res) == k:
                    return res