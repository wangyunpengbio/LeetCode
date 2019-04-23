class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 使用动态规划,矩阵的每个元素表示该地方到终点的路径数，行列各自多一行方便计算，超出的那行列为0，表示无法到达。
        matrix = [[0 for j in range(m+1)] for i in range(n+1)]
        matrix[n-1][m-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:continue
                # 每个位置到达的路径数为：该位置右侧的路径数 + 该位置下侧的路径数
                matrix[i][j] = matrix [i+1][j] + matrix[i][j+1]
        # print(matrix)
        return matrix[0][0]