class Solution:
    # 广度优先遍历，会超时
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # 测试当前位置是否合适，pathSet负责存储走过的路径
        def testCurrentGold(i,j,pathSet):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 0:
                return False
            if (i,j) in pathSet:
                return False
            return True
        # 搜索四个方向
        def search(result,i,j,pathSet):
            if testCurrentGold(i,j,pathSet):
                search(result, i + 1, j, pathSet | set([(i,j)]) )
                search(result, i - 1, j, pathSet | set([(i,j)]) )
                search(result, i ,j + 1, pathSet | set([(i,j)]) )
                search(result, i ,j - 1, pathSet | set([(i,j)]) )
            else:
                result.append(pathSet)
        # 试遍历起始点，整个矩阵每个位置都可以当做起点
        result = []
        for i in range(m):
            for j in range(n):
                if testCurrentGold(i,j,set()):
                    search(result,i,j,set())
        # 计算该路径上黄金总量
        def calculateGold(pathSet):
            currentPathGold = 0
            for item in pathSet:
                currentPathGold += grid[item[0]][item[1]]
            return currentPathGold
        # 找出最大黄金数量的路径
        maxGold = 0
        for pathSet in result:
            maxGold = max(calculateGold(pathSet),maxGold)
        return maxGold
