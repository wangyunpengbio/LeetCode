# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 利用栈进行二叉树的前序遍历
        if root == None:
            return None
        stack = [root]
        while len(stack) != 0:
            cur = stack.pop()
            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
            cur.left = None  # 记得将左子树置空
            cur.right = stack[-1] if len(stack) != 0 else None # 如果是最后一个元素，则链表的末尾为空
            