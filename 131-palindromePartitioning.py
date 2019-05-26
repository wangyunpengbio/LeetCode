class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 深度优先搜索
        def dfs(results,result,s):
            if len(s) == 0:
                results.append(result[:])
                return None
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    dfs(results,result + [s[:i+1]],s[i+1:])
        results = []
        dfs(results,[],s)
        # print(results)
        return results
                