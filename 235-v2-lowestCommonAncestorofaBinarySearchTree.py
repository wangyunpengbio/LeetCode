# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 非递归写法
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - q.val) * (root.val - p.val) > 0:
            # print(root.val,p.val,q.val)
            if q.val > root.val and p.val > root.val:
                root = root.right
            if q.val < root.val and p.val < root.val:
                root = root.left
        return root