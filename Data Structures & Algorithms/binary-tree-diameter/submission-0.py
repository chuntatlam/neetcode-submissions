'''
max width of binary tree passing through a node is
max depth of left branch + max depth of right branch
use a dfs to get the max left and max right of each node
keep track of max width with a variable, updating it each time a bigger max is found
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            max_left_depth = dfs(root.left)
            max_right_depth = dfs(root.right)
            res = max(res, max_left_depth + max_right_depth)
            return 1 + max(max_left_depth, max_right_depth)
        dfs(root)
        return res

        