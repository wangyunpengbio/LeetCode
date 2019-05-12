# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 跟二叉树的层次遍历一样，先用辅助的level遍历完了以后再排序
        if root == None:return []
        queue = [(root,0)]
        res = []
        while len(queue) != 0:
            item,level = queue.pop(0)
            if item != None:
                res.append([item.val,level])
                queue.append((item.left,level+1))
                queue.append((item.right,level+1))
        maxDepth = res[-1][-1]
        results = [[] for i in range(maxDepth + 1)]
        for item,level in res:
            results[maxDepth - level].append(item)
        return results