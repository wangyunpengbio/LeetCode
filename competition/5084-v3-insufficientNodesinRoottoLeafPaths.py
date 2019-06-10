# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        dic = {}
        def dfs(dic,curSum,node):
            if node == None:
                return curSum
            else:
                curSum += node.val
                leftSum = dfs(dic,curSum,node.left)
                rightSum = dfs(dic,curSum,node.right)
                path_sum = max(leftSum, rightSum)
                dic[node] = path_sum
                return path_sum
        dfs(dic,0,root)
        # 从字典和树中,删除不足节点
        flag = True
        while flag:
            flag = False
            for node,value in dic.items():
                if node.left != None and dic[node.left] < limit:
                    dic.pop(node.left)
                    node.left = None
                    flag = True
                    break
                if node.right != None and dic[node.right] < limit:
                    dic.pop(node.right)
                    node.right = None
                    flag = True
                    break
        if dic[root] < limit:return None
        return root