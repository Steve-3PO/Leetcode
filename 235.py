# Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        while True:
            
            # if the node value is larger than both p and q, go left
            if root.val > q.val and root.val > p.val:
                root = root.left
                
            # if the node value is smaller than both p and q, go right
            elif root.val < q.val and root.val < p.val:
                root = root.right
                
            else:
                return root