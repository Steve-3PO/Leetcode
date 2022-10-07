# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Monotonic Decreasing Stack
        # create a stack and add each element to it, when moving onto the next element, pop the stack top if it is a temperature increase
        
        # initialise a stack
        stack = []
        
        # default array of 0s, this means we dont need to create code for when temperature never increases
        res = [0] * len(temperatures)
        
        # track the temperature and the index of each input
        for i, temp in enumerate(temperatures):
            
            # when the current temp is larger than the stop stack temp,
            while stack and temp > stack[-1][0]:
                
                # pop the value and use its logged index to find the difference to the current index
                t, j = stack.pop()
                res[j] = i - j
            
            # append element to the stack
            stack.append((temp, i))
        return res