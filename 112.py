# Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            
        # define a search function with a sum and node input
        def search(s, node):
            
            # check if there is a node
            if node is not None:
                
                # if exists find the new sum
                new_sum = s + node.val
                
                # run search left with new sum
                left = search(new_sum, node.left)
                
                # run search right with new sum
                right = search(new_sum, node.right)
                   
                # return when new_sum == target and it is a leaf node
                return left or right or (new_sum == targetSum and (node.left is None and node.right is None))
                
            return False
                    
        
        return search(0, root) if root else False