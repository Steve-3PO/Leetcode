# Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # start hare and tortoise pointers at the beginning
        h = t = head
        
        # while the hare can move you know the tortoise is always in the middle
        while h != None and h.next != None:
            h = h.next.next
            t = t.next
        
        return t