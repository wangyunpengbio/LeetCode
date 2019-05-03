class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 所有起始点的所有可能，会超时
        def dfs(results,result,board,position):
            m = len(board)
            n = len(board[0])
            # 如果越界或者已经重复走,则表示结束
            if  position[0] > m-1 or position[1] > n-1 or board[position[0]][position[1]] == "*" \
            or position[0] < 0 or position[1] < 0:
                # print("".join(result))
                results.append("".join(result))
            else:
                c = board[position[0]][position[1]]
                result.append(c)
                board[position[0]][position[1]] = "*"
                dfs(results,result,board,(position[0]+1,position[1]))
                dfs(results,result,board,(position[0],position[1]+1))
                dfs(results,result,board,(position[0]-1,position[1]))
                dfs(results,result,board,(position[0],position[1]-1))
                # 每次注意恢复原来的board
                board[position[0]][position[1]] = c
                result.pop()
        results = []
        # 全部起始点都有可能
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(results,[],board,(i,j))
        # print(results)
        # 查看是否存在于结果中
        for item in results:
            if word in item:
                return True
        return False