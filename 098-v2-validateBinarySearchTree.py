# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历为升序 则为二叉搜索树
        def inorderTraversal(root: TreeNode):
            res = []
            if not root: # 如果根是空的话
                return []
            else:
                res.extend(inorderTraversal(root.left))
                res.append(root.val)
                res.extend(inorderTraversal(root.right))
                return res
        res = inorderTraversal(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
