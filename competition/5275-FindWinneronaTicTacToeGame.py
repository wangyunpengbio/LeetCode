class Solution:
    # 用list记录横、竖，左右对角线 同一线上棋子数量，然后判断是否有3个即可
    def tictactoe(self, moves: List[List[int]]) -> str:
        from collections import defaultdict
        A = [defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)]
        B = [defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)]
        for i,step in enumerate(moves):
            if i % 2 == 0:
                A[0][step[0]] += 1
                A[1][step[1]] += 1
                A[2][step[0]+step[1]] += 1
                A[3][step[0]-step[1]] += 1
            else:
                B[0][step[0]] += 1
                B[1][step[1]] += 1
                B[2][step[0]+step[1]] += 1
                B[3][step[0]-step[1]] += 1
        def checkWin(list4dic):
            def checkdic(dic):
                for k,v in dic.items():
                    if v == 3:
                        return True  
                return False
            for dic in list4dic:
                if checkdic(dic):
                    return True
            return False
        if checkWin(A):
            return "A"
        elif checkWin(B):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"