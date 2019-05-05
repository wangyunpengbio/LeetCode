class Solution:
    # 超出时间限制
    def multi(self,n):
        result=1
        for i in n:
            result=result * i
        return result
    def minScoreTriangulation(self, A: List[int]) -> int:
        # 深度优先搜索，遍历所有可能性
        def dfs(results,result,A):
            # print(results)
            if len(A)==3:
                res = self.multi(A)
                result.append(res)
                results.append(result[:])
                result.pop()
                return None
            else:
                for i in range(len(A)):
                    res = self.multi([A[i-1],A[i],A[(i+1)%len(A)]])
                    result.append(res)
                    left = A[:i]+A[i+1:]
                    dfs(results,result,left)
                    result.pop()
        results = []
        dfs(results,[],A)
        # print(results)
        minRes = sum(results[0])
        for item in results:
            minRes = min(minRes,sum(item))
        return minRes