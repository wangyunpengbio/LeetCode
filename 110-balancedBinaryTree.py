# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 辅助函数：计算当前节点的深度
        def calculateDepth(root):
            maxDepth = 0
            if root == None: # 如果当前节点为空，则直接为0
                return maxDepth
            else:
                maxDepth = maxDepth + 1 # 如果当前节点不为空，则先把深度 +1，再计算左右子树的深度加上去
                if root.left != None:
                    maxDepth = max(maxDepth, calculateDepth(root.left) + 1)
                if root.right != None:
                    maxDepth = max(maxDepth, calculateDepth(root.right) + 1)
                # print(root.val,leftDepth,rightDepth)
                return maxDepth
        # 当前节点为空，则为平衡
        if root == None:
            return True
        else:
            depthLeft = calculateDepth(root.left)
            depthRight = calculateDepth(root.right)
            # print("------")
            # print(root.val,depthLeft,depthRight)
            # print("------")
            # 如果当前子树不平衡，则为假
            if abs(depthLeft - depthRight) > 1:
                return False
            else:
                # 如果当前子树的左右也不平衡，也为假
                if self.isBalanced(root.left) and self.isBalanced(root.right):
                    return True
                else:
                    return False