# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 基于递归
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            res = []
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
            return res