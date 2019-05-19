# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def backtracking(root):
            if root == None:
                return 1
            left = backtracking(root.left)
            if left == 0:
                return 0
            right = backtracking(root.right)
            if right == 0:
                return 0
            return max(left, right)+1 if abs(left - right)<=1 else 0
        if root == None:
            return True
        if backtracking(root) != 0:
            return True
        else:
            return False
