"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        rawStartNode = node
        dic = {} # dic为 原始节点 -> 新的节点
        # 先广度优先遍历，创建好节点
        queue = [node]
        while len(queue) != 0:
            cur = queue.pop(0)
            if cur not in dic:
                newCur = Node(cur.val,None)
                dic[cur] = newCur
                for node in cur.neighbors: # 把当前节点的邻居中，在字典里都已经创建好了，把没在字典里的放到queue中等待创建
                    if node not in dic:
                        queue.append(node)
        # 再根据字典，把边连起来
        for originNode,cloneNode in dic.items():
            newNodelist = []
            for neighbor in originNode.neighbors:
                newNodelist.append(dic[neighbor])
            cloneNode.neighbors = newNodelist
        return dic[rawStartNode]
