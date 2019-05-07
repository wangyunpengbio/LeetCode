# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 基于栈的做法
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur != None or len(stack) != 0: # 当前节点为空，并且栈空的时候，结束遍历
            if cur != None:                   # 先遍历root树，再右子树，最后左子树；即中右左
                stack.append(cur)             # 由于是逆序，则变成左右中
                res.insert(0,cur.val)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res