# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # first we must set a start to the list called "head" and assign it the same class as the nodes
        head=ListNode()
        
        # By assigning head to t, we point head towards t, the start of the list.
        t=head
    
        # while there are elements in each list we compare
        while list1 and list2:
            
            # compare the values of the current nodes
            if list1.val < list2.val:
                
                # assigns a pointer from t to the next list1 value
                t.next = ListNode(list1.val)
                
                # move along the list
                list1 = list1.next
                
            # othewise assigns pointer to the list2 value
            elif list1.val >= list2.val:
                t.next = ListNode(list2.val)
                list2 = list2.next
                
            # move along t
            t = t.next
        

        # autopopulate list if it exists while the other doesn't
        if list1 is not None:
            t.next=list1
        if list2 is not None:
            t.next=list2
            
        # return the head which points to the first element in the list
        return head.next