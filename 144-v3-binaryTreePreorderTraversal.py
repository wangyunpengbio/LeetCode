# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 基于栈的做法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return []
        stack = [root]
        while len(stack) != 0:
            cur = stack.pop()
            res.append(cur.val) # 最先把当前根节点的值输出
            if cur.right != None: # 再先压入右子树，后压入左子树，栈先进后出，最后变成先左子树再右子树
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
        return res