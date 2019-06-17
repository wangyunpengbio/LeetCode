# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 层次遍历，记下每个节点的层数，当前层的位置，然后造好结果列表对应着改就可以了
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if root == None:return [[]]
        records = []
        queue = [(1,1,root)]
        while len(queue) != 0:
            level,index,node = queue.pop(0)
            if node.left != None:
                queue.append((level+1,2*index-1,node.left))
            if node.right != None:
                queue.append((level+1,2*index,node.right))
            records.append((level,index,node.val))
        maxlevel = records[-1][0]
        results = [["" for i in range(2**maxlevel-1)]for j in range(maxlevel)]
        for level,index,value in records:
            # 2**(maxlevel-level)-1为每一行前面的空格数目
            # 2**(maxlevel+1-level)为每一行的元素间隔的空格数目
            results[level-1][2**(maxlevel-level)-1 + (index-1)* 2**(maxlevel+1-level) ] = str(value)
        return results