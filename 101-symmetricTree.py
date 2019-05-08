# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归做法，如果一个树的左子树与右子树镜像对称，那么这个树是对称的。
        def isMirror(tree1,tree2):
            if tree1 == None and tree2 != None:return False
            if tree1 != None and tree2 == None:return False
            if tree1 == None and tree2 == None:return True         
            if tree1.val == tree2.val and isMirror(tree1.left,tree2.right) and isMirror(tree1.right,tree2.left):
                return True
            else:
                return False
        if root==None:
            return True
        return isMirror(root.left,root.right)
                