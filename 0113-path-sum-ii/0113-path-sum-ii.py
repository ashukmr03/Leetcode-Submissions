# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []
        def traverse(node, cs, path):
            if node is None:
                return
            cs += node.val
            path.append(node.val)
            # Found a root-to-leaf path
            if node.left is None and node.right is None:
                if cs == targetSum:
                    ans.append(path[:])  # store a copy, not the same list
            else:
                traverse(node.left, cs, path)
                traverse(node.right, cs, path)
            # Backtrack: remove this node before returning to its parent
            path.pop()
        traverse(root, 0, [])
        return ans