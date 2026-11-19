# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def bst(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = bst(left, mid)
            node.right = bst(mid + 1, right)
            return node
        return bst(0, len(nums))