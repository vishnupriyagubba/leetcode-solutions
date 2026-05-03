# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.dia = 0
        def helpt(node):
            if not node:
                return 0
            lh = helpt(node.left)
            rh = helpt(node.right)
            self.dia = max(self.dia,lh + rh)
            return 1 + max(lh,rh)
        helpt(root)
        return self.dia


        