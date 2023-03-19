# Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # we want to stop immediately if there is not tree
        if not preorder or not inorder:
            return None

        # the root of a tree is always the first in the preorder
        root = TreeNode(preorder[0])

        # the value of the first preorder index within the inorder tree will determine the left to right partitions
        mid = inorder.index(preorder[0])

        # everything on the left of the root on the inorder tree will be in the left subtree, recalling the function
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # everything on the right of the root on the inorder tree will be in the right subtree, recalling the function
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root