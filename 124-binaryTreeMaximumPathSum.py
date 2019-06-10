# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 记录整棵树的最大路径
        self.resMax = float("-inf")
        def calculateCurrentMax(dic, root): # dic字典保存已经计算过的节点
            if root == None:
                return 0
            else:
                if dic.get(root.left):
                    leftValue = dic.get(root.left)
                else:
                    leftValue = calculateCurrentMax(dic,root.left)
                    dic[root.left] = leftValue
                if dic.get(root.right):
                    rightValue = dic.get(root.right)
                else:
                    rightValue = calculateCurrentMax(dic,root.right)
                    dic[root.right] = rightValue
                # 当前节点计算出的最大值，有四种可能路径，左中，右中，左中右，中
                self.resMax = max(self.resMax, leftValue + root.val, rightValue + root.val,
                                    leftValue + rightValue + root.val,
                                    root.val)
                # print(self.resMax,root.val)
                # 而当前节点保存的路径最大值只有，左，右，中三种，左中右无法同时同时接到上层
                return max(leftValue + root.val,
                           rightValue + root.val,
                           root.val)
        dic = {}
        calculateCurrentMax(dic, root)
        return self.resMax