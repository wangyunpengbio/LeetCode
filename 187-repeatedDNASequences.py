class Solution:
    # 动态规划
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set() # 集合去除重复
        N = len(s)
        dp = [[0 for i in range(N+1)] for j in range(N+1)]
        # 两序列一横一竖排好，然后左上到右下，每个值表示当前能完全匹配多长
        for i in range(1,N+1):
            for j in range(i+1,N+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] >= 10:
                    res.add(s[i-10:i])
        return list(res)