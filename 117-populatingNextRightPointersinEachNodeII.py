"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = [(1,root)]
        lastLevel = 1
        fillLevelQueue = []
        while len(queue) != 0:
            level,item = queue.pop(0)
            if level == lastLevel + 1: # 临时的列表存完一层，就进行结点连接吗，然后再清空该列表
                nodeNum = len(fillLevelQueue)
                fillLevelQueue.append(None)
                for i in range(nodeNum):
                    fillLevelQueue[i].next = fillLevelQueue[i+1]
                    # print("line"+str(i))
                lastLevel = lastLevel + 1
                fillLevelQueue = []
            if item == None: # 如果层中间遍历到空结点，就不追加，层最后遍历到空结点也不追加
                continue
            fillLevelQueue.append(item) # 每次遍历到结点的时候，顺便把结点存到另一个列表中
            # print(item.val)
            queue.append((level + 1,item.left))
            queue.append((level + 1,item.right))
        return root
            