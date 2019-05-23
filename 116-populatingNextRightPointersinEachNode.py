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
    # 层次遍历，每遍历完一层，就把当前层的结点连起来
    def connect(self, root: 'Node') -> 'Node':
        if root == None: # 如果根节点为空，直接返回空(其实此题可以不加这个)
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
            if item == None: #遍历到最后一层的下面，就会出现None，直接break
                break
            fillLevelQueue.append(item) # 每次遍历到结点的时候，顺便把结点存到另一个列表中
            # print(item.val)
            queue.append((level + 1,item.left))
            queue.append((level + 1,item.right))
        return root
            