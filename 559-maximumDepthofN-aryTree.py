"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    # 广度优先遍历
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        res = 0
        queue = [(root,1)]
        while len(queue) != 0:
            item,level = queue.pop(0)
            res = max(res,level)
            for child in item.children:
                queue.append((child,level+1))
        return res