# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        queue1 = deque([root.left])
        queue2 = deque([root.right])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.right)
            queue2.append(node2.left)
        # Both queues must become empty together
        return not queue1 and not queue2