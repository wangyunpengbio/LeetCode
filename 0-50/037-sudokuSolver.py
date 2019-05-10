class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 检查当前位置填了现在要填的数字后，数独是否有效
        def checkShuDu(board,singlePos,numToFeed):
            numToFeed = str(numToFeed)
            x,y = singlePos
            for item in board[x]:
                if item == numToFeed:
                    return False
            for j in range(len(board)):
                if board[j][y] == numToFeed:
                    return False
            boxXleft,boxXright = x//3*3,(x//3+1)*3
            boxYleft,boxYright = y//3*3,(y//3+1)*3
            for i in range(boxXleft,boxXright):
                for j in range(boxYleft,boxYright):
                    if board[i][j] == numToFeed:
                        return False
            return True
        
        def dfs(results,board,position,level):
            # 如果要填的位置都填满了
            if len(position) == level:
                results.append( [[] for i in range(len(board)) ])
                for i in range(len(board)):
                    results[-1][i] = board[i][:]
                return True
            singlePos = position[level]
            for i in range(1,10):
                if checkShuDu(board,singlePos,i):
                    board[singlePos[0]][singlePos[1]] = str(i)
                    # dfs(results,board,position,level+1)   # 搜到一个结果就全部返回停止遍历了
                    if dfs(results,board,position,level+1): # 如果当前位置能填好，就进行下一个位置的遍
                        return True
                    board[singlePos[0]][singlePos[1]] = '.'
        
        # 计算出全部需要加数字的位置
        position = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    position.append((i,j))
        results = []
        dfs(results,board,position,0)
