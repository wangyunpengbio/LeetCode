# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
审题出现了问题，不足节点不是像现在这样从上到下的累加
而是从下到上的累加，然后去最大值
'''
class Solution:
    # 先将每个节点到根的累计求和算出来，再删掉不符合情况的叶子
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root == None:return []
        rootZero = TreeNode("zero")
        rootZero.left = root
        # 先把树的节点->对应值,父节点,左右,保存下来
        records = {}
        queue = []
        records[root] = (root.val,rootZero,"left")
        queue.append(root)
        while len(queue)!=0:
            item = queue.pop(0)
            if item.left != None:
                records[item.left] = (item.left.val,item,"left")
                queue.append(item.left)
            if item.right != None:
                records[item.right] = (item.right.val,item,"right")
                queue.append(item.right)
        # 计算叶子到根的累计求和类似使用队列进行BFS
        queue = []
        queue.append(root)
        while len(queue)!=0:
            item = queue.pop(0)
            if item.left != None:
                item.left.val = item.val + item.left.val
                queue.append(item.left)
            if item.right != None:
                item.right.val = item.val + item.right.val
                queue.append(item.right)
        # 从字典和树中,删除不足节点
        flag = True
        while flag:
            flag = False
            for node,(rawvalue,Upnode,direction) in records.items():
                # print(node,(rawvalue,Upnode,direction))
                if node.left == None and node.right == None and node.val < limit:
                    if direction == "left":
                        Upnode.left = None
                    if direction == "right":
                        Upnode.right = None
                    # print("del")
                    records.pop(node)
                    flag = True
                    break
        for node,(rawvalue,Upnode,direction) in records.items():
            node.val = rawvalue
        return rootZero.left
