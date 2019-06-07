class Solution:
    # 超时 优化后的深度优先遍历，找出所有匹配，在找的时候如果发现不一样就跳过
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
                    if s[i] == t[level]:
                        dfs(results,result+s[i],s[i+1:],t,level+1)
        results = []
        dfs(results,"",s,t,0)
        # print(results)
        return len(results)
            