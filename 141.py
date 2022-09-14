# Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # to find a link in a list we need a hare and tortoise pointer pair
        h = head
        t = head
        
        # while the hare can move forward, we must have not reached the end of the list
        while h is not None and h.next is not None:
            h = h.next.next
            t = t.next
            
            # return if they meet
            if t == h:
                return True
            
        return False