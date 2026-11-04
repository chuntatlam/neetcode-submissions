'''
dfs with a stack
starting with root in stack
check if stack is empty
if not empty, pop the top element in stack
check is top element is not None
if not None, add the left and right child nodes to the stack
use a depth variable to keep track of depth at each node
update res variable at each step to keep track of max depth
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node: # not None
                res = max(res, depth) # res update needs to be after checking node is valid
                stack.append((node.left, 1 + depth))
                stack.append((node.right, 1 + depth))
        
        return res
        