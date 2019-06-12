# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root