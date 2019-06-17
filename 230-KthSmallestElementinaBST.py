# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 非递归的做法 中序遍历 找到第k个元素就停止
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        stack = []
        cur = root
        while cur != None or len(stack) != 0: # 当前节点为空，并且栈空的时候，结束遍历
            if cur != None:
                stack.append(cur)             # 如果当前节点不为空，就入栈
                cur = cur.left                # 先遍历左子树
            else:
                cur = stack.pop()             # 如果当前节点为空了，就出栈，curr指向要出栈的那个节点，即要开始返回了
                res.append(cur.val)           # 从左子树返回的时候，把节点值放入数组
                cur = cur.right               # 遍历右子树
                if len(res) == k:
                    return res[-1]
