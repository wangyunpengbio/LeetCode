# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 递归的做法 中序遍历 找到第k个元素就停止
        def inorderTraversal(res,root,k):
            if not root: # 如果根是空的话
                return None
            else:
                if inorderTraversal(res,root.left,k):return True
                res.append(root.val)
                if len(res) == k:
                    return True
                if inorderTraversal(res,root.right,k):return True
        res = []
        inorderTraversal(res,root,k)
        return res[-1]