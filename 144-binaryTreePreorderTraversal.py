# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 基于递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            res = []
            res.append(root.val)
            res.extend(self.preorderTraversal(root.left))
            res.extend(self.preorderTraversal(root.right))
            return res