class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 深度优先遍历，先把不围绕的区域标T，然后再把围绕的区域标X，T转回O
        def dfs(board,i,j):
            if not (0 <= i <= len(board) - 1) or not (0 <= j <= len(board[0]) - 1): # 如果越界，则不继续染色
                return None
            elif board[i][j] == "O": # 如果当前是O的话，才继续染色
                board[i][j] = "T"
                dfs(board,i+1,j)
                dfs(board,i-1,j)
                dfs(board,i,j+1)
                dfs(board,i,j-1)
            else:
                return None
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 如果在边界上，且为O，就染色成T，顺带把相邻的O都染成T
                if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
                    # print(i,j)
                    dfs(board,i,j)
        # 把T转回成O，把O转成X
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 如果在边界上，且为O，就染色成T，顺带把相邻的O都染成T
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"