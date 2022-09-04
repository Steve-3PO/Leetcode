# Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if no head exists, return
        if not head: return
    
        # create hare and tortoise pointers at head
        t, h = head,head
        
        # while hare can move 2 and tortoise move 1
        while h.next and h.next.next:
            t = t.next
            h = h.next.next
            
            # break when they meet
            if h == t: break
        
        # remove edge cases where loop ties to -1st node
        if not h.next or not h.next.next: return
    
        # create a second tortoise pointer
        t2 = head
    
        # while the first tortoise can move, move both t pointers
        while t.next:
            if t == t2: return t
            t = t.next
            t2 = t2.next
            
        return