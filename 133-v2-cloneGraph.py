"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 深度优先遍历 非递归
        if node == None :return None
        resNode2CopyNode = {}
        stack = [node]
        copy = Node(node.val,None)
        resNode2CopyNode[node] = copy
        while stack:
            current = stack.pop()
            neighbors = current.neighbors
            if neighbors == None:continue # 原来图里该节点就没有邻居，直接跳过
            copyNode = resNode2CopyNode[current]
            if copyNode.neighbors == None:
                copyNode.neighbors = []
            # 遍历当前节点的全部邻居，把“当前节点的拷贝”的邻居list也拷贝好，遇到新邻居:创建新节点，新节点放到stack中；遇到旧邻居:直接从dic中拿节点
            for nei in neighbors:
                if nei in resNode2CopyNode:
                    copyneighbor = resNode2CopyNode[nei]
                else:
                    copyneighbor = Node(nei.val,None)
                    resNode2CopyNode[nei] = copyneighbor
                    stack.append(nei)
                copyNode.neighbors.append(copyneighbor)
        return copy