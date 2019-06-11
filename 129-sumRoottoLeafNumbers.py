# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(curSum,node):
            if node == None:
                return curSum
            else:
                curSum = curSum * 10 + node.val
                leftSum = dfs(curSum,node.left)
                rightSum = dfs(curSum,node.right)
                path_sum = leftSum + rightSum
                # print(node.val,curSum,leftSum,rightSum,node.left,node.right)
                # 如果左右两边同时空，或者同时有值，说明该结点是对称的，和为两边加起来
                if (node.right == None and node.left == None) or (node.right != None and node.left != None):
                    return path_sum
                else: # 如果两边不对称，就只要最大的那个
                    return max(leftSum,rightSum)
        allSum = dfs(0,root)
        return int(allSum/2)