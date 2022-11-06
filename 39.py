# Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # require a result array to append combinations to
        res = []
        
        # create function that takes in a position i, current and total values 
        def dfs(i, cur, total):
            
            # stop if at target, append current array into res 
            if total == target:
                res.append(cur.copy())
                return
            
            # stop if outside len
            if i >= len(candidates) or total > target:
                return
                
            # append cur with the current value and do not move i for next dfs
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            # also use a dfs without adding adding, to create solutions that do not use the indexed value, moving along the list
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res