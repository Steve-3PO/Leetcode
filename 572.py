# Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # no subtree is technically a subtree of every tree, there true        
        if not subRoot:
            return True
        
        # no parent tree means no subtree can exist     
        if not root:
            return False
        
        # check for same nodes in tree        
        if self.sameTree(root, subRoot):
            return True
        
        # if no match is found run the function again on the lower trees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    # this function checks whether the nodes of a tree and subtree are equal     
    def sameTree(self, root, subRoot):
        
        # if the nodes dont exist then they are technically equal
        if not root and not subRoot:
            return True
        
        # if nodes exist and are the same, continue recalling this function on the next children
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) 
        
        # all other occurences 
        return False
        