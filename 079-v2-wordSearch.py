class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(result,board,position,k,word): # k表示当前是比较word第几个字符
            if len(result)==1:return True # 如果已经找到了,直接返回True，全部不遍历了
            # print(position,k)
            if k >= len(word): # 如果此时k也正好准备越界,则表明正好匹配（前面的全都匹配上了，相对于找到了）
                result.append(True)
                return True
            m = len(board)
            n = len(board[0])
            # 如果越界或者已经重复走,则表示结束
            if  position[0] > m-1 or position[1] > n-1 or board[position[0]][position[1]] == "*" \
            or position[0] < 0 or position[1] < 0:
                pass
                # if k >= len(word): # 如果此时k也正好准备越界,则表明正好匹配
                #     result.append(True)
                #     return True
                # else: # 如果k还有剩下的字符,则表明无法匹配
                #     return False
            else:
                c = board[position[0]][position[1]]
                if word[k]==c:
                    board[position[0]][position[1]] = "*"
                    dfs(result,board,(position[0]+1,position[1]),k+1,word)
                    dfs(result,board,(position[0],position[1]+1),k+1,word)
                    dfs(result,board,(position[0]-1,position[1]),k+1,word)
                    dfs(result,board,(position[0],position[1]-1),k+1,word)
                    # 每次注意恢复原来的board
                    board[position[0]][position[1]] = c
                else:
                    return False
        # 全部起始点都有可能
        result = []
        for i in range(len(board)-1,-1,-1):
            for j in range(len(board[0])-1,-1,-1):
                # print("%d_%d"%(i,j))
                dfs(result,board,(i,j),0,word)
                if result:
                    return True
        return False