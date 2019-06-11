class Solution:
    # 动态规划，再造一个[[]]来存储到当前位置最小的路径长度
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        for i in range(1,len(triangle)):
            dp.append([])
            dp[-1].append(triangle[i][0] + dp[i-1][0])
            for j in range(1,len(triangle[i])-1):
                dp[-1].append(triangle[i][j] + min(dp[i-1][j-1],dp[i-1][j]))
            dp[-1].append(triangle[i][-1] + dp[i-1][-1])
        # print(dp)
        return min(dp[-1])