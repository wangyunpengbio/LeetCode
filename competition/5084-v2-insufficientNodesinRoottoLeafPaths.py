# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(node, sum_):
            if not node:
                return sum_, sum_ >= limit
            sum_ += node.val
            left, lf = dfs(node.left, sum_)
            right, rf = dfs(node.right, sum_)
            if not lf:
                node.left = None
            if not rf:
                node.right = None
            path_sum = max(left, right)
            return path_sum, path_sum >= limit
        sum_, flag = dfs(root, 0)
        if not flag:
            return None
        return root