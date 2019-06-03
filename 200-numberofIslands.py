class Solution:
    # 深度优先遍历
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,grid,level):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return None
            else:
                if grid[i][j] == "0":
                    return None
                elif grid[i][j] == "1":
                    grid[i][j] = str(level)
                    dfs(i+1,j,grid,level)
                    dfs(i-1,j,grid,level)
                    dfs(i,j+1,grid,level)
                    dfs(i,j-1,grid,level)
                else:
                    return None
        res = 0
        level = 11 # 为了不与岛屿的表示方法"1"重复，初始设为11，每遇到新的岛屿+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j,grid,level)
                    res = level - 10
                    level = level + 1
        # for item in grid:
            # print(item)
        return res