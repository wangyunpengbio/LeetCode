class Solution:
    # 广度优先遍历，能通过更多案例，还是会超时
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def testCurrentGold(i,j,pathSet):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 0:
                return False
            if (i,j) in pathSet:
                return False
            return True
        # 优化了搜索中结束时加入path的方式，原来同一条路径，会以向上向右向左向下四个方向结束，同一路径结束时会加入四次，现在只会加入一次
        def search(result,i,j,pathSet):
            flagCount = 0
            if testCurrentGold(i + 1, j, pathSet):
                search(result, i + 1, j, pathSet | set([(i + 1,j)]))
                flagCount += 1
            if testCurrentGold(i - 1, j, pathSet):
                search(result, i - 1, j, pathSet | set([(i - 1,j)]))
                flagCount += 1
            if testCurrentGold(i ,j + 1, pathSet):
                search(result, i ,j + 1, pathSet | set([(i,j + 1)]))
                flagCount += 1
            if testCurrentGold(i ,j - 1, pathSet):
                search(result, i ,j - 1, pathSet | set([(i,j - 1)]))
                flagCount += 1
            if flagCount == 0: # 四条路都走不通，到头了
                result.append(pathSet)
        result = []
        for i in range(m):
            for j in range(n):
                if testCurrentGold(i,j,set()):
                    search(result,i,j,set([(i,j)]))
        def calculateGold(pathSet):
            currentPathGold = 0
            for item in pathSet:
                currentPathGold += grid[item[0]][item[1]]
            return currentPathGold
        maxGold = 0
        for pathSet in result:
            maxGold = max(calculateGold(pathSet),maxGold)
        return maxGold
