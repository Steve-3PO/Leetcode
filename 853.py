# Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # first must pair car distances and speeds together and then sort by starting position as the front cars will always stop cars behind we must iterate from the furthers along
        pair = [[p, s] for p, s in zip(position, speed)]
        pair = sorted(pair)

        # require a stack to append cars to that do not collide
        stack = []
        
        # for each car in reverse order (max distance to min)
        for p, s in pair[::-1]:

            # calculate the time required to get to target
            time = (target - p) / s 

            # if there is a car ahead of it, check if its a shorter time, as this means it will collide
            if stack and time <= stack[-1]:
                continue
            else:
                # otherwise add the slower car time
                stack.append(time)
        
        # return the length as this is the number of cars that are leading each fleet
        return len(stack)