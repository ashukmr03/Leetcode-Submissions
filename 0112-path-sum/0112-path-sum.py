# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def traverse(node,cs):
            if node is None:
                return False
            cs+=node.val
            if node.left is None and node.right is None:
                return cs==targetSum
            return (
                traverse(node.left,cs) or 
                traverse(node.right,cs)
            )
        return traverse(root,0)