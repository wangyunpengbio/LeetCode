# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    # 直接借助队列进行层次遍历，找每层最右边的节点即可
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:return []
        res = defaultdict(list)
        queue = [(root,0)]
        while len(queue) != 0:
            item,level = queue.pop(0)
            res[level].append(item.val)
            if item.left != None:
                queue.append((item.left,level+1))
            if item.right != None:
                queue.append((item.right,level+1))
        results = []
        for key,values in res.items():
            results.append(values[-1])
        return results