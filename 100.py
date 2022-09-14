# Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # if neither nodes exist, then the trees are the same
        if not q and not p:
            return True
        
        # if both exist with sam value then the trees are the same, return the function on the node children
        if q and p and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # all other cases are false
        else:
            return False