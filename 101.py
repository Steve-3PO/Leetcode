# Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # define a function that compared left and right values
        def compare(left, right):
            
            # return True if both are None
            if left is None and right is None:
                return True
            
            # return the comparison of the children nodes if values are equal
            elif left and right and left.val == right.val:
                return compare(left.left, right.right) and compare(left.right, right.left)
            
            # all other cases are False
            else:
                return False
            
            
        return compare(root.left, root.right)