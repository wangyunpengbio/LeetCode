# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 先中序遍历，中序遍历应该是升序，找到排列错误的两个节点，交换值
        def midTraversal(res,root):
            if root != None:
                midTraversal(res,root.left)
                res.append(root)
                midTraversal(res,root.right)
        res = []
        midTraversal(res,root)
        # for i in res:
            # print(i.val)
        start,end = None,None # 初始化待交换的两个节点
        for i in range(len(res) - 1):
            if res[i].val > res[i+1].val and start == None: # start赋值以后，就不重复赋值了
                start = res[i]
            if res[i].val > res[i+1].val:
                end = res[i+1]
        start.val,end.val = end.val,start.val
