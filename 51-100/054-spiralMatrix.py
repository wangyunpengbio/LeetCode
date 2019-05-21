class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 将已经走过的地方置None，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向：
        if matrix == []:return []
        res = []
        rownums = len(matrix)
        colnums = len(matrix[0])
        row = 0
        col = 0
        direction = ["r","b","l","u"] # 四个方向，依次是右下左上
        curDirIndex = 0
        while len(res) != rownums*colnums:
            # print(row,col,res)
            if 0 <= row < rownums and 0 <= col < colnums and  matrix[row][col] != None:
                res.append(matrix[row][col])
                matrix[row][col] = None
            else:
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
        return res