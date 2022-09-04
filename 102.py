# Binary Tree Level Order Traversal

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if there is no root then we return the empty list
        if not root:
            return []
        
        
        # empty list for storing the values
        total = []
    
        # must use a queue to store values as we arrive at them
        queue = collections.deque()
    
        # first value in the queue will be the root
        queue.append(root)
        
        
        # while there are elements in the queue
        while queue:
        
            # the sublists will be the length of the queued elements
            sub_list = len(queue)
    
            # create an empty list for the sublists
            items_in_sublist = []
    
            # iterating n times for each sublist
            for _ in range(sub_list):
        
                # take the first element of the queue
                node = queue.popleft()
    
                # add the popped element to the list of sublists
                items_in_sublist.append(node.val)
                
                # before adding the sublist to the total list, check if there are 
                # children to the node selected, appending the queue if True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                # add the sublist to the total list
            total.append(items_in_sublist)
        return total
            