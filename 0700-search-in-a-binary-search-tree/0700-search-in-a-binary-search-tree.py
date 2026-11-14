# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def search(node,val):
            if node is None:
                return None
            if(node.val==val):
                return node
            if node.val>val:
                return search(node.left,val)
            else:
                return search(node.right,val)
        return search(root,val)