# Remove Duplicates from Sorted List

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a set for all values seen so far
        seen = set()
        
        # remove edge case, add the first value to the set
        if head is not None:
            seen.add(head.val)
        else:
            return
        
        # create a pointer to the start of the list
        root = ListNode()
        root.next = head
        
        # checking next element
        while head.next:
            
            # if not seen yet we can add value to seen and move head onward
            if head.next.val not in seen:
                seen.add(head.next.val)
                head = head.next
            
            # if value in seen then we skip over the node
            else:
                head.next = head.next.next
        
        # call the pointer to the start of the list
        return root.next