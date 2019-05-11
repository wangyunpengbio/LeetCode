# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归 其实还有很多种解法，比如把树层次遍历也可以，遍历的时候记录下当前的层数
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))