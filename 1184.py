# Distance Between Bus Stops

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        
        # if start is before destination
        if start < destination:

            # direct
            route1 = 0
            for val in distance[start:destination]:
                route1 += val
        
            # not direct
            route2 = 0
            for val in distance[:start]:
                route2 += val
            for val in distance[destination:]:
                route2 += val

            # return the minimum
            return min(route1, route2)

        # if start is after
        if start > destination:

            # direct
            route1 = 0
            for val in distance[destination:start]:
                route1 += val
        
            # not direct
            route2 = 0
            for val in distance[start:]:
                route2 += val
            for val in distance[:destination:]:
                route2 += val

            # return the minimum
            return min(route1, route2)