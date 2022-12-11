# Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        # need total for title
        total = 0
        @cache

        # define search function with nonlocal total
        def summ(root):
            nonlocal total

            # return instantly of no value
            if not root:
                return 0

            # find the total tilt of left and right sides, return the sum upwards
            x = root.val + summ(root.left) + summ(root.right)
            total += abs(summ(root.right) - summ(root.left))
            
            return x

        summ(root)

        return total