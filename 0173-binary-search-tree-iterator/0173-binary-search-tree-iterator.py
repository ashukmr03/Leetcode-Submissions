# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
    def next(self) -> int:
        if not self.stack[-1].right:
            return self.stack.pop().val
        else:
            ans=self.stack.pop()
            rot=ans.right
            while rot:
                self.stack.append(rot)
                rot=rot.left
            return ans.val
    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()