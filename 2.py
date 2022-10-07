# Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a node to start the new list, initialise a carry number and a current pointer
        new = ListNode()
        current = new
        carry = 0
        
        # while there is a number to use
        while l1 or l2 or carry:
            
            # default to 0 if node is empty
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            
            # sum of vals and carry is the current value
            new_val = first_val + second_val + carry
            
            # floor operator used to find carry number, if 0 remains 0, if 10-19 sets to 1
            carry = new_val // 10
            
            # new value is always the modulus of 10, if less than 10 remains unchanged
            new_val = new_val % 10
                
            # append new value
            current.next = ListNode(new_val)
            
            # move along
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return new.next