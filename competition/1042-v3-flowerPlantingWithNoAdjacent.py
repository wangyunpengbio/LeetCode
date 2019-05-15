class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # 深度优先遍历 将check函数进一步优化，查询是否有效不再使用列表循环，而是字典直接查找
        # 能通过更多测试用例，无法全部通过
        from collections import defaultdict
        # 将花园之间的连接关系用字典存储，gardenID -> {与gardenID相连的那些gardenID}，如果path中有[1,2]和[2,1]的话会重复，所以值用set集合存储
        graph = defaultdict(set)
        for path in paths:
            graph[path[0]].add(path[1])
            graph[path[1]].add(path[0])
        # print(graph)
        
        def check(color,graph,level,candidateColor): # level表示当前备选的花园，candidateColor表示当前备选的颜色
            gardenID = level + 1
            for item in graph[gardenID]: # 遍历当前garden连接的所有garden
                if color[item - 1] == candidateColor: # item - 1为当前遍历的garden的id
                    return False
            # 如果已经种花的地方全部通过验证，则通过
            return True
        
        color = ["*"] * N
        def dfs(color,level): # level表示当前备选花园
            if "*" not in color:
                return True
            # 四种颜色
            for i in range(1,5):
                if check(color,graph,level,candidateColor=i): # 检查当前备选花园 是否可以种 当前备选颜色
                    color[level] = i
                    if dfs(color,level+1):
                        return True
                    color[level] = "*"
        dfs(color,0)
        return color