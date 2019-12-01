class Solution:
    # 动态规划，找出解（超时）
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        col = min(tomatoSlices//4,cheeseSlices//1) + 1
        row = min(tomatoSlices//2,cheeseSlices//1) + 1
        matrix = [[False for i in range(col)] for j in range(row)]
        for j in range(row):
            matrix[j][0] = (2 * j,1 * j)
            if matrix[j][0][0] == tomatoSlices and matrix[j][0][1] == cheeseSlices:
                    return [0,j]
            for i in range(1,col):
                matrix[j][i] = (matrix[j][i-1][0]+4,matrix[j][i-1][1]+1)
                if matrix[j][i][0] == tomatoSlices and matrix[j][i][1] == cheeseSlices:
                    return [i,j]
                if matrix[j][i][0] > tomatoSlices or matrix[j][i][1] > cheeseSlices:
                    break
        # for item in matrix:
        #     print(item)
        return []
