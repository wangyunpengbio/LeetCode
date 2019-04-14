class Solution:
    def isMatch(self,s, p):
        m=len(s)
        n=len(p)
        dp = [[bool(0) for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = bool(1)
        # 开始初始化填充,如果匹配的串s是空的的话，只有模式是*才能匹配
        for j in range(n):
            if dp[0][j] and p[j] == '*':
                dp[0][j + 1] = bool(1)

        ## 开始动态规划
        for i in range(m):
            for j in range(n):
                # * dp[i][j+1]表示 *匹配任意一个字符  dp[i+1][j]表示 *匹配0个字符
                if p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j+1] or dp[i+1][j]
                # 把? 当成普通字符一起匹配。这个就比较简单当前位置一样，或者是. 并且[i-1][j-1]也是要匹配
                elif p[j] == '?' or s[i] == p[j]:
                    dp[i+1][j + 1] = dp[i][j]
                # 第二个else语句等价于下面这个
                # else:  dp[i+1][j + 1] = dp[i][j] and (p[j] == '?' or s[i] == p[j])
        return dp[m][n]