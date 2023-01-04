# Maximum Value of a String in an Array

class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        # variable to track max value
        max_seen = 0

        # iterate through list
        for st in strs:

            # if str is numeric we can use int()
            if st.isnumeric():
                max_seen = max(max_seen, int(st))

            # otherwise we use the length of the string
            else:
                max_seen = max(max_seen, len(st))

        return max_seen