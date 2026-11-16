# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = TreeNode(val)
        if not root:
            return node
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = node
                    break
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = node
                    break
                cur = cur.left
        return root