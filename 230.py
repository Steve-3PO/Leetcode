# Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # initialise a stack and a current node pointer
        stack = []
        current = root
        
        # when current is none, we can pop from the stack assuming the stack is not none
        while current is not None or stack is not None:
            
                # continue moving down left side of the tree
                while current is not None:
                    
                    stack.append(current)
                    current = current.left
                
                # reaching a current = none node ends the while loop and we can pop our last stack element
                current = stack.pop()
                
                # subtract 1 from k as the value will be the smallest current value
                k -= 1
                
                # when k is 0 we know it is the value we want
                if k == 0:
                    return current.val
                
                current = current.right