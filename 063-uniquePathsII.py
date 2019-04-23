class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 使用动态规划,矩阵的每个元素表示该地方到终点的路径数
        m,n = len(obstacleGrid[0]),len(obstacleGrid)
        matrix = [[0 for j in range(m)] for i in range(n)]
        # 如果对应的位置是有障碍物，则无法到达终点，路径数为0
        matrix[n-1][m-1] = 1 if obstacleGrid[n-1][m-1] != 1 else 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:continue
                # 分成右侧和下侧两部分，如果某一部分超出或者有障碍物，则该部分对应值为0，最后把两部分值相加即可
                if i+1 < n and obstacleGrid[i+1][j] != 1:
                    down = matrix [i+1][j]
                else:
                    down = 0
                if j+1 < m and obstacleGrid[i][j+1] != 1:
                    right = matrix[i][j+1]
                else:
                    right = 0
                matrix[i][j] = down + right
                # 如果该位置有障碍，则重置值为0
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
        # print(matrix)
        return matrix[0][0]