class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划，矩阵中每个位置存储从当前位置到终点的最小路径和
        m = len(grid)
        n = len(grid[0])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:continue
                # 如果越界的话，则无法到达终点，对应方向的路径和为无限大
                if i+1 < m:
                    down = grid[i+1][j]
                else:
                    down = float("inf")
                if j+1 < n:
                    right = grid[i][j+1]
                else:
                    right = float("inf")
                # print(down,right)
                grid[i][j] = grid[i][j] + min(down,right)
        # print(grid)
        return grid[0][0]