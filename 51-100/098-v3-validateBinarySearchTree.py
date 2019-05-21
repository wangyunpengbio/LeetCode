# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归法
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTdiy(root: TreeNode, leftLimit, rightLimit) -> bool:
            if(root==None):
                return True
            if(root.val<=leftLimit or root.val>=rightLimit):
                return False
            return isValidBSTdiy(root.left,leftLimit,root.val) and isValidBSTdiy(root.right,root.val,rightLimit)
        
        return isValidBSTdiy(root,-float("inf"),float("inf"))
