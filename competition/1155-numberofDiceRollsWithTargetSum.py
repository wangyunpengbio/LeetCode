class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7 ## 题目要求取模
        dp = [[0 for i in range(1010)] for j in range(31)] #行：骰子数，列target的值
        for i in range(1,f+1):
            dp[1][i] = 1
        for i in range(1,d+1):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if j - k >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-k]) # 扔 i 个骰子 ，可以看做是已经扔了 i-1 个骰子(总和为 Target-k)，然后再扔最后一个骰子(值为k)，可能的种类数目: 扔 i-1 个骰子，总和 Target-k
        return dp[d][target] % mod