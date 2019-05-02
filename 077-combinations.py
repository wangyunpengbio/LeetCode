class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 深度优先搜索
        def dfs(results,result,n,k,level):
            if len(result)==k:
                results.append(result[:])
            elif len(result) > k:
                pass
            else:
                for item in range(level,n+1):
                    result.append(item)
                    dfs(results,result,n,k,level=item+1)
                    result.pop()
        results = []
        dfs(results,[],n,k,level=1)
        return(results)