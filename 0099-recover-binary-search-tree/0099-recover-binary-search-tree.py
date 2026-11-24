# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, prev, anomaly1, anomaly2):
        if node is None:
            return prev, anomaly1, anomaly2
        prev, anomaly1, anomaly2 = self.traverse(
            node.left, prev, anomaly1, anomaly2
        )
        if prev is not None and prev.val > node.val:
            if anomaly1 is None:
                anomaly1 = prev
            anomaly2 = node
        prev = node
        return self.traverse(node.right, prev, anomaly1, anomaly2)
    def recoverTree(self, root: TreeNode | None) -> None:
        prev, anomaly1, anomaly2 = self.traverse(
            root, None, None, None
        )
        temp = anomaly1.val
        anomaly1.val = anomaly2.val
        anomaly2.val = temp