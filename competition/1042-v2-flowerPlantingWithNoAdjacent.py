class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # 优化了check函数，依旧超出时间限制
        # check函数，检查当前花园种了当前颜色的花，是否会产生“邻接种植相同花的情况”而不符合要求
        def check(color,paths,level,candidateColor): # level表示当前备选的花园，candidateColor表示当前备选的颜色
            for path in paths:
                gardenID1 = path[0] - 1
                gardenID2 = path[1] - 1
                if level != gardenID1 and level != gardenID2: # 如果当前路径无关，则跳过
                    continue
                if color[gardenID1] == candidateColor or color[gardenID2] == candidateColor: # 当前路径有关，如果有相同颜色则跳过
                    return False
            # 如果已经种花的地方全部通过验证，则通过
            return True
        
        color = ["*"] * N
        def dfs(color,level): # level表示当前备选花园
            if "*" not in color:
                return True
            # 四种颜色
            for i in range(1,5):
                if check(color,paths,level,candidateColor=i): # 检查当前备选花园 是否可以种 当前备选颜色
                    color[level] = i
                    if dfs(color,level+1):
                        return True
                    color[level] = "*"
        dfs(color,0)
        return color