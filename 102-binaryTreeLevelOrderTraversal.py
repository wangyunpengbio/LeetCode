# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 类似使用队列进行BFS，每次顺带记录当前的层数
        if root == None:return []
        records = []
        queue = []
        queue.append((root,0))
        while len(queue)!=0:
            item,level = queue.pop(0)
            if item == None:
                pass
            else:
                records.append((item.val,level))
                queue.append((item.left,level+1))
                queue.append((item.right,level+1))
        # 最后将存储(结点值,层数)的二元组进行后续处理
        maxlevel = records[-1][-1]
        results = [[] for i in range(maxlevel+1)]
        for item,level in records:
            results[level].append(item)
        return(results)
