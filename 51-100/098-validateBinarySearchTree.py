# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历为升序 则为二叉搜索树
        res = [-float("inf")]  # res记录最近输出的那个值
        stack = []
        cur = root
        while cur != None or len(stack) != 0: # 当前节点为空，并且栈空的时候，结束遍历
            if cur != None:
                stack.append(cur)             # 如果当前节点不为空，就入栈
                cur = cur.left                # 先遍历左子树
            else:
                cur = stack.pop()             # 如果当前节点为空了，就出栈，curr指向要出栈的那个节点，即要开始返回了
                # 如果最新输出的值比之前的值要小，则中序遍历出现降序，不正确
                if res.pop() < cur.val:
                    res.append(cur.val)       # 从左子树返回的时候，把节点值放入数组
                else:
                    return False
                cur = cur.right               # 遍历右子树
        return True
