# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #No root node, so tree has a depth of 0
        if not root:
            return 0
        
        #if there is a root node we confirm there is a depth of at least 1
       
        #return 1 + the max of the calling the function on the root node of left and right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        