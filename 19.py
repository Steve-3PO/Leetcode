# Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # With left and right pointers we can separate them by n so that once r meets the end of the list, l is on the node we want to alter. Require a temp node at the start to eliminate edge case [1], n=1
        tmp = ListNode(0, head)
        l = tmp
        r = head
        
        
        # more right pointer along n times
        while n > 0:
            r = r.next
            n -= 1
            
        # move both pointers along till end of list
        while r is not None:
            l = l.next
            r = r.next
            
        # assign the node 2 steps ahead to the position 1 step ahead
        l.next = l.next.next
        
        return tmp.next