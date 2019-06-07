class Solution:
 # dp[i][j]二维数组，用来表示 T中前i个字符 与 S中前j个字符 对应的可行的序列个数。
 # * 动态规划 但是效率并不高 20ms 35.83%
 # *    *  b  a  b  g  b  a  g
 # * *  1  1  1  1  1  1  1  1
 # * b  0  1  1  2  2  3  3  3
 # * a  0  0  1  1  1  1  4  4               #  b  a  b  g  b  a   4=3(3个b)+1(1个ba)
 # * g  0  0  0  0  1  1  1  5               #  b  a
 # * param s
 # * param t
 # * return
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        dp[0] = [1 for i in range(len(s))]
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        return dp[-1][-1]
