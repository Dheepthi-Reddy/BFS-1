'''
In this problem, given a binary tree, we need to find the level order traversal nodes.
To solve this, I took a queue, since queue works as FIFO, as I popped the first element and stored it in a temporary array, and its child nodes to the end of queue.
As we pop the elements, I took a size variable on queue, and maintained the list of lists. 
The no.of elements of queue at the that time equal to no.of elements on the list/level of the tree.
So, every time we iterate on the tree as many times as the size, and create lists. 
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        result = []
        queue = [root]
        # as long as we have elements in the queue
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                # popping the first element and adding to a temporary list
                curr = queue.pop(0)
                temp.append(curr.val)
                # adding children of each node to the queue as long as they exist
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # adding the list of nodes to the result list
            result.append(temp)
        
        return result

'''
Time Complexity: O(n)
Because we are traversing through all the nodes once.
Time Complexity: O(n)
Maximum no of nodes we can have in the queue at a time is equal to the width of the tree, which is n/2, since we can ignore constants O(n)
'''   