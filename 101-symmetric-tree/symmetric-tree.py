# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def helpt(p,q):
            if not p and not q:
                return True
            if  not p or not q:
                return False
            if p.val != q.val:
                return False
            lt = helpt(p.left,q.right)
            rt = helpt(p.right,q.left)
            if lt and rt:
                return True
            else:
                return False
        return helpt(root.left,root.right)
        



        