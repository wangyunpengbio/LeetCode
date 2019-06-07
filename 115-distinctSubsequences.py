class Solution:
    # 超时 深度优先遍历，找出所有匹配
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(results,result,s,t,level):
            if level == len(t):
                if result == t:
                    results.append(result)
                return None
            elif level > len(t):
                return None
            else:
                for i in range(len(s)):
                    dfs(results,result+s[i],s[i+1:],t,level+1)
        results = []
        dfs(results,"",s,t,0)
        return len(results)
            