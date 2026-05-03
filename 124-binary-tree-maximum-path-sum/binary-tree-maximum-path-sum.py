# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def helpt(node):
            if not node:
                return 0
            lh = max(helpt(node.left),0)
            rh = max(helpt(node.right),0)
            curr = node.val+lh+rh
            self.max_sum = max(self.max_sum,curr)
            return node.val + max(lh,rh)
        helpt(root)
        return self.max_sum

       

        