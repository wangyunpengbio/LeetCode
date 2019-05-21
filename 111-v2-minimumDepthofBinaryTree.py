# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 类似于层次遍历 利用队列，队列中每个元素为(节点,层数)
        if root == None:
            return 0
        level = 1
        queue = [(root,1)]
        while len(queue) != 0: # 由于是二叉树，迟早会有叶子节点(无子节点)
            item,level = queue.pop(0)
            if item.left == None and item.right == None:
                return level
            if item.left != None:
                queue.append((item.left,level+1))
            if item.right != None:
                queue.append((item.right,level+1))
                