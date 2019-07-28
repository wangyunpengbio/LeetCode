class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 把字符的位置记录下来
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        coordinate = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                coordinate[board[i][j]] = (i,j)
        # 寻找路径
        def singleAlphabet(start,end):
            curPath = ""
            startrow,startcol = coordinate[start]
            endrow,endcol  = coordinate[end]
            # 由于Z单独一行，注意这四个方向的顺序
            if startrow > endrow:
                curPath = curPath + "U" * (startrow - endrow)
            if startcol > endcol:
                curPath = curPath + "L" * (startcol - endcol)
            if startrow < endrow:
                curPath = curPath + "D" * (endrow - startrow)
            if startcol < endcol:
                curPath = curPath + "R" * (endcol - startcol)
            return curPath + "!"
        target = "a" + target
        res = ""
        for i in range(1,len(target)):
            res = res + singleAlphabet(target[i-1],target[i])
        return res