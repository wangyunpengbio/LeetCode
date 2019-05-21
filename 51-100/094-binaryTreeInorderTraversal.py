# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归的做法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: # 如果根是空的话
            return []
        else:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
            return res