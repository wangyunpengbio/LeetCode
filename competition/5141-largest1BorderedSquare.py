class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # 验证正方形
        def validate(start,end):
            startrow,startcol = start
            endrow,endcol = end
            # for i in range(startrow,endrow+1):
            #     for j in range(startcol,endcol+1):
            #         if i == startrow or i == endrow or j == startcol or j == endcol:
            #             if grid[i][j] != 1:
            #                 return False
            for i in range(startrow,endrow+1):
                if grid[i][startcol] != 1:
                    return False
            for i in range(startrow,endrow+1):
                if grid[i][endcol] != 1:
                    return False
            for j in range(startcol,endcol+1):
                if grid[startrow][j] != 1:
                    return False
            for j in range(startcol,endcol+1):
                if grid[endrow][j] != 1:
                    return False
            return True
        res = 0
        # 注意加速运算，找到符合的大小，直接从头算下一个大小是否存在
        for level in range(0,min(len(grid),len(grid[0]))):
            flag = False
            for i in range(len(grid)):
                if flag:break
                for j in range(len(grid[0])):
                    # print("---",(i,j),(i+level,j+level),"---")
                    if i+level < len(grid) and j+level < len(grid[0]) and validate((i,j),(i+level,j+level)):
                        res = max(res,level+1)
                        flag = True
                        break
        return res*res