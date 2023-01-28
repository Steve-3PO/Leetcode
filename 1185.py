# Day of the Week

import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # require hashmap to track which day of the week as the weekday() returns a number for day of the week
        hashmap = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

        return hashmap[calendar.weekday(year, month, day)]