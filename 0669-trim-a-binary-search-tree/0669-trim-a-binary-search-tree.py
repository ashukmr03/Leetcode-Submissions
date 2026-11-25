# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        head = TreeNode(0, None, root)
        def traverse(node, prev):
            original = node
            while node and (node.val < low or node.val > high):
                if node.val < low:
                    node = node.right
                else:
                    node = node.left
            if prev.left is original:
                prev.left = node
            else:
                prev.right = node
            if node is None:
                return
            traverse(node.left, node)
            traverse(node.right, node)
        traverse(root, head)
        return head.right