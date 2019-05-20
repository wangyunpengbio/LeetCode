class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 检查当前结果是否正确
        def test(result):
            rowSet = set()
            colSet = set()
            ZCrossSet = set() # 正对角就是相减只差一样的(左上到右下)
            FCrossSet = set() # 负对角就是相加之和一样的
            for i in range(len(result)):
                for j in range(len(result[i])):
                    if result[i][j] == "Q":
                        if i in rowSet or j in colSet or i - j in ZCrossSet or i + j in FCrossSet:
                            return False
                        rowSet.add(i)
                        colSet.add(j)
                        ZCrossSet.add(i - j)
                        FCrossSet.add(i + j)
            return True
        # 深度优先搜索
        def dfs(results,result,rowlevel,n,numQueue):
            if numQueue == n:#rowlevel == n and collevel == n and
                results.append(["".join(item) for item in result])
                return None
            for row in range(rowlevel,n):
                for col in range(0,n): # 因为column有可能是先(0,1)，再(1,3)，接着回到(2,0)，所以col必须都从0重新开始
                    result[row][col] = "Q"
                    if test(result):
                        dfs(results,result,row + 1,n,numQueue + 1) # row可以直接跳到下一行
                    result[row][col] = "."
            
        results = []
        result = [["." for i in range(n)] for j in range(n)]
        dfs(results,result,0,n,0)
        return results