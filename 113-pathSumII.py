# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 深度优先遍历，和上一题基本一致，多了一个列表记录路径
        def dfs(results,result,root,curSum,tarSum): # 调用的时候注意了root不为空
            # print(root.val,curSum)
            if curSum == tarSum and root.left==None and root.right == None: # 如果求和满足，并且是叶子节点，则返回True
                results.append(result[:])
                return None
            else:
                if root.left != None: # 如果左子树非空，则加上左子树的值再遍历(只在函数传值的时候增加)
                    result.append(root.left.val)
                    dfs(results,result,root.left,curSum + root.left.val,tarSum)
                    result.pop() # 还要再把元素pop出
                if root.right != None:# 如果右子树非空，则加上右子树的值再遍历
                    result.append(root.right.val)
                    dfs(results,result,root.right,curSum + root.right.val,tarSum)
                    result.pop()
        if root == None:
            return []
        else:
            results = []
            dfs(results,[root.val],root = root,curSum = root.val,tarSum = sum) # 初始的和 为根节点的值
            return results