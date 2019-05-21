class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 转化为二分法查找的问题
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        left,right = 0,m*n-1
        while(left<=right):
            # middle当前查找的是相对于整个矩阵，当前二分法正中间的多少位
            middle = int((left + right)/2)
            # position计算出中间值对应的矩阵坐标
            position = (middle//n,middle%n)
            # print(middle,position)
            if matrix[position[0]][position[1]] > target:
                right = middle - 1
            elif matrix[position[0]][position[1]] < target:
                left = middle + 1
            else:
                return True
        return False