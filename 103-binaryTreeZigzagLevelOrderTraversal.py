# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 和上一题层次遍历一样，只不过最后根据level层数进行了翻转
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:return []
        res = {}
        level = 0
        queue = [(root,level)]
        while len(queue) != 0:
            cur,level = queue.pop(0)
            if cur == None:
                continue
            else:
                res.setdefault(level,[]).append(cur.val) # 如果当前level还没有生成list，则为赋值为空列表[]
                queue.append((cur.left,level+1))
                queue.append((cur.right,level+1))
        # 找出最大层数
        maxlevel = max(res.keys())
        results = [[] for i in range(maxlevel+1)]
        for key,value in res.items():
            if key % 2 == 1: # 如果层数为奇数，则翻转该层结果
                value.reverse()
            results[key] = value
        return results

