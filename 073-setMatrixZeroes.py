class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 时间复杂度O(mn), 空间复杂度O(m+n)
        m, n = len(matrix), len(matrix[0])
        row_v = [False] * m
        col_v = [False] * n
        for i in range(m): # 行
            for j in range(n): # 列
                if(matrix[i][j] == 0):
                    row_v[i] = True
                    col_v[j] = True
        for ii in range(m):
            for jj in range(n):
                if(row_v[ii] == True or col_v[jj] == True):
                    matrix[ii][jj] = 0
        return None