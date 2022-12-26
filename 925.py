# Long Pressed Name

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # if name is shorter than typed always return false
        if len(typed) < len(name):
            return False

        # initialise a previous variable to track the last seen character in name
        prev = 0

        # keep iterating until typed is covered
        while typed:

            # if chars are the same, shorten both string, and keep the char in a prev variable
            if name and name[0] == typed[0]:
                prev = name[0]
                name = name[1:]
                typed = typed[1:]
            
            # in the case name no longer exists but type does, check if typed char is the same as the last char (prev) from name
            elif prev == typed[0]:
                typed = typed[1:]

            # if not typed char is not equal to current name char or prev, must be false
            else:
                return False

        # must consider edge case where typed shortens to 0 while name does not
        return True if not name and not typed else False