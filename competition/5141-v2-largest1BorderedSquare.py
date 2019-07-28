class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        f = [[0] * m for _ in range(n)]
        g = [[0] * m for _ in range(n)]
        for i in range(n):
            f[i][0] = grid[i][0]
            for j in range(1, m):
                f[i][j] = 0 if grid[i][j] == 0 else f[i][j - 1] + 1
        print(f)
        for j in range(m):
            g[0][j] = grid[0][j]
            for i in range(n):
                g[i][j] = 0 if grid[i][j] == 0 else g[i - 1][j] + 1
        print(g)
        for ret in range(min(n, m), 0, -1):
            for i in range(n):
                for j in range(m):
                    # 只要四条边都符合，即可。可是这里的含义有点问题，因为i - ret + 1和j - ret + 1有可能是负数，最好是补上判断
                    if f[i][j] >= ret and g[i][j] >= ret and f[i - ret + 1][j] >= ret and g[i][j - ret + 1] >= ret:
                        return ret * ret
        return 0