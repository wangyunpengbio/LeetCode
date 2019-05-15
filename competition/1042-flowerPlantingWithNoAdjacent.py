class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # 深度优先遍历 超出时间限制
        # 查看当前种花方式，已经种花的花园 是否有邻接种植相同花的情况
        def check(color,paths):
            for path in paths:
                gardenID1 = path[0] - 1
                gardenID2 = path[1] - 1
                # 如果当前花园还没种花，则跳过
                if color[gardenID1] == "*" or color[gardenID2] == "*":
                    continue
                if color[gardenID1] == color[gardenID2]:
                    return False
            # 如果已经种花的地方全部通过验证，则通过
            return True
        
        color = ["*"] * N
        def dfs(color,level):
            if "*" not in color:
                return True
            # 四种颜色
            for i in range(1,5):
                color[level] = i
                if check(color,paths):
                    if dfs(color,level+1):
                        return True
                else:
                    color[level] = "*"
        dfs(color,0)
        return color