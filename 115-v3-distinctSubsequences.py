import functools
class Solution:
    # 暴力搜索加上lru_cache，注意cache别开太大，不然会超出内存限制
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(maxsize=30200)
        def dfs(s1, s2):
            if not s2: return 1                # 如果t为空，则只有全不选这一种可能
            if len(s1) < len(s2): return 0     # 如果s长度小于t，则没有可能
            if len(s2)==1:
                return s1.count(s2)
            if s1==s2: return 1
            if s1[0] == s2[0]:
                return dfs(s1[1:], s2) + dfs(s1[1:], s2[1:])
            else:
                return dfs(s1[1:], s2)
        return dfs(s, t)
            