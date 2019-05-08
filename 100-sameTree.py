# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 跟101基本一致
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 基于递归
        # 俩结点同时为空，则为真
        if p == None and q == None:return True
        # 基于上面那个if语句，俩结点有一个非空，如果再有一个空，则一空一非空，则为假
        if p == None or q == None:return False
        # 比较当前结点值，左子树以及右子树
        if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else:
            return False
