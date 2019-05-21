class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for row in range(n)]
        direction = ["r","b","l","u"] # 四个方向，依次是右下左上
        curDirIndex = 0
        i = row = col = 0 # 全都初始化为0
        while i < n*n:
            # print(matrix,i)
            if 0 <= row < n and 0 <= col < n and  matrix[row][col] == None:
                i = i + 1
                matrix[row][col] = i
            else: # 如果越界了，或者已经赋过值了，就改方向
                if direction[curDirIndex] == "r":
                    col = col - 1
                elif direction[curDirIndex] == "b":
                    row = row - 1
                elif direction[curDirIndex] == "l":
                    col = col + 1
                elif direction[curDirIndex] == "u":
                    row = row + 1
                curDirIndex = (curDirIndex + 1) % 4
            if direction[curDirIndex] == "r":
                col = col + 1
            elif direction[curDirIndex] == "b":
                row = row + 1
            elif direction[curDirIndex] == "l":
                col = col - 1
            elif direction[curDirIndex] == "u":
                row = row - 1
        return matrix