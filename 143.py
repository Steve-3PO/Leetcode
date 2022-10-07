# Reorder List 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
                
        # First must find center of list
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
        
        # from the center we reverse the second half of the list
        secondhalf = tortoise.next
        
        # separate the 2 lists temporarily 
        tortoise.next = None
        prev = None
        
        while secondhalf:
            newhead = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = newhead
        
        # 2 pointers, 1 at the beginning of first list, and 1 at the new start of the second
        firsthalf = head
        secondhalf = prev
        
        # reassign list, requiring 2 temp variables to store next values
        while secondhalf is not None:
            tmp1 = firsthalf.next
            tmp2 = secondhalf.next
            firsthalf.next = secondhalf
            secondhalf.next = tmp1
            
            firsthalf = tmp1
            secondhalf = tmp2