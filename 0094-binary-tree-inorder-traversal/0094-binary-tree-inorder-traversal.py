# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=[]
        def Traversal(root):
            if(root==None):
                return
            Traversal(root.left)
            ans.append(root.val)
            Traversal(root.right)
        Traversal(root)
        return ans