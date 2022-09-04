# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        
#       while a head exists we set a placeholder, newhead, to the next value

        while head:
            newhead = head.next
            
#           then set the next value to the previous value, or None at string start

            head.next = prev
    
#           now set previous value to the value of the current node
#           and the placeholder containing the value of head.next can be assigned
#           to the current head, this makes the sequence take a step back
            prev = head
            head = newhead

        return prev