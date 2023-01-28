# Determine if Two Events Have Conflict

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        #hrs
        event1starthour = int(event1[0][:2])
        event1endhour = int(event1[1][-5:-3])
        event2starthour = int(event2[0][:2])
        event2endhour = int(event2[1][-5:-3])

        #mins
        event1startmin = int(event1[0][3:5])
        event1endmin = int(event1[1][-2:])
        event2startmin = int(event2[0][3:5])
        event2endmin = int(event2[1][-2:])

        # rather than check all conditions that overlap, simply check the only instances it doesnt and return True for all other cases
        if event2starthour > event1endhour or (event2starthour == event1endhour and event2startmin > event1endmin):
            return False
        
        elif event1starthour > event2endhour or (event1starthour == event2endhour and event1startmin > event2endmin):
            return False

        else:
            return True