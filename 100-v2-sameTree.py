# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 跟101基本一致
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       # 该算法的工作原理类似于 BFS，但存在一些关键差异。每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。
        queue = []
        queue.append(p)
        queue.append(q)
        while(len(queue)!=0):
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 == None and t2 == None:continue
            if t1 == None or t2 == None:return False
            if t1.val != t2.val:return False
            queue.append(t1.left)
            queue.append(t2.left)
            queue.append(t1.right)
            queue.append(t2.right)
        return True
