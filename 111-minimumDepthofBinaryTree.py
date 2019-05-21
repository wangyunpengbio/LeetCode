# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root != None and root.left == None and root.right == None: # 叶子节点，无子节点
            return 1
        elif root != None and root.left != None and root.right == None: # 有左子树
            return self.minDepth(root.left) + 1
        elif root != None and root.left == None and root.right != None: # 有右子树
            return self.minDepth(root.right) + 1
        elif root != None and root.left != None and root.right != None: # 左右子树都有
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
        elif root == None: # 因为上面都不会传空节点进来，所以如果传入了空节点，那么一定是0深度的二叉树
            return 0