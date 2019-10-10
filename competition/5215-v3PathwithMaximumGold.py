class Solution:
    # 直接把set改成list就可以了，set每次加入数据的时候会进行去重
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def testCurrentGold(i,j,pathList):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 0:
                return False
            if (i,j) in pathList:
                return False
            return True
        def search(result,i,j,pathList):
            flagCount = 0
            if testCurrentGold(i + 1, j, pathList):
                search(result, i + 1, j, pathList + [(i + 1, j)])
                flagCount += 1
            if testCurrentGold(i - 1, j, pathList):
                search(result, i - 1, j, pathList + [(i - 1, j)])
                flagCount += 1
            if testCurrentGold(i ,j + 1, pathList):
                search(result, i ,j + 1, pathList + [(i, j + 1)])
                flagCount += 1
            if testCurrentGold(i ,j - 1, pathList):
                search(result, i ,j - 1, pathList + [(i, j - 1)])
                flagCount += 1
            if flagCount == 0: # 四条路都走不通，到头了
                result.append(pathList)
        result = []
        for i in range(m):
            for j in range(n):
                if testCurrentGold(i,j,[]):
                    search(result,i,j,[(i,j)])
        def calculateGold(pathList):
            currentPathGold = 0
            for item in pathList:
                currentPathGold += grid[item[0]][item[1]]
            return currentPathGold
        maxGold = 0
        for pathList in result:
            maxGold = max(calculateGold(pathList),maxGold)
        return maxGold
