# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        level = 1
        queue = [(root,1)]
        while len(queue) != 0:
            item,level = queue.pop(0)
            if item.left == None and item.right == None:
                return level
            if item.left != None:
                queue.append((item.left,level+1))
            if item.right != None:
                queue.append((item.right,level+1))
                