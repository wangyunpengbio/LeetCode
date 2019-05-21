# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 深度优先遍历
        def dfs(root,curSum,tarSum): # 调用的时候注意了root不为空
            # print(root.val,curSum)
            if curSum == tarSum and root.left==None and root.right == None: # 如果求和满足，并且是叶子节点，则返回True
                return True
            else:
                if root.left != None: # 如果左子树非空，则加上左子树的值再遍历(只在函数传值的时候增加)
                    if dfs(root.left,curSum + root.left.val,tarSum): # 如果左子树深度遍历满足，则一层层返回True
                        return True
                if root.right != None:# 如果右子树非空，则加上右子树的值再遍历
                    if dfs(root.right,curSum + root.right.val,tarSum):
                        return True
                return False # 如果左右子树遍历都不行，则返回空
        if root == None:
            return False
        else:
            return dfs(root = root,curSum = root.val,tarSum = sum) # 初始的和 为根节点的值