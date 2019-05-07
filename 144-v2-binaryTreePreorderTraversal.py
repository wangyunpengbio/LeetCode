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
        stack = []
        cur = root
        while cur != None or len(stack) != 0: # 当前节点为空，并且栈空的时候，结束遍历
            if cur != None:
                res.append(cur.val)           # 如果当前节点不为空，就把当前值先输出
                stack.append(cur.right)       # 再把右子树入栈
                cur = cur.left                # 再遍历左子树
            else:
                cur = stack.pop()
        return res