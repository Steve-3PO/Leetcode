# Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # initialise root queue and answer array
        q = [root]
        answer = []
        
        # while there are elements in the queue
        while len(q) > 0:
            
            # iterate n times (n = len(q)) the length of the queue before continually appending
            for i in range(n := len(q)):
                
                # if the popped value exists
                if (c:=q.pop(0)) is not None: 
                    
                    # when i reaches the length of the original queue - 1, it must be the last element of that level so we append
                    if i == n-1: 
                        answer.append(c.val)
                        
                    # append children nodes if they exist
                    if c.left is not None: q.append(c.left)
                    if c.right is not None: q.append(c.right)
                    
        return answer