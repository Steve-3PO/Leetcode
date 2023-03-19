# Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # want to create a hashmap mapping all courses to their prereq's
        # then we dfs through each course and its pre-reqs till we find courses that can be completed without pre-reqs
        # we return up the tree and if we ever find a course we cant, we return false

        # create hashmap with all courses and default no pre-reqs
        premap = { i : [] for i in range(numCourses)}

        # populate our hashmap with all inputs
        for course, prereq in prerequisites:
            premap[course].append(prereq)

        # need a visit set to find course loops that cant be completed along the dfs path
        visit = set()

        # need a dfs function to work along paths of courses
        def dfs(course):

            # first thing we check is if its in visit set as this means its part of a loop
            if course in visit:
                return False

            # if no pre-reqs for this course its the end of a path and we return True upwards
            if premap[course] == []:
                return True
            
            # if it is neither 2 conditions above we add the course to the set and move down its prereqs
            visit.add(course)
            for pre in premap[course]:

                # if we ever get a value we want to return False again
                if not dfs(pre): return False
            
            # remove set and make the prereqs empty, creating a new end of the path so we dont need to check over again
            visit.remove(course)
            premap[course] = []

            # if it has not returned False then we return True at the end
            return True

        # we must check each course individually as this might not be one large tree but several smaller ones
        for course in range(numCourses):

            # return false as soon as we cant take a course
            if not dfs(course): return False
        return True