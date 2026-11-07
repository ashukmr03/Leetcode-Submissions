# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            # Both are None: this position matches
            if node1 is None and node2 is None:
                continue
            # One is None, or values differ
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            # Add children even if they are None,
            # so structural gaps are compared at the same position
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)
        # Both queues must become empty together
        return not queue1 and not queue2