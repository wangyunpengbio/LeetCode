# 超时
class Solution:
    def numSquares(self, n: int) -> int:
        # 测试当前数字是否为平方数
        def test_perfect_squares(n):
            if n**(0.5)%1 != 0:
                return False
            else:
                return True
        # 动态规划，F(i) = min{ F(i-1)+F(1), F(i-2)+F(2), F(i-3)+F(3)...F(2)+F(i-2), F(1)+F(i-1) }
        dp = [0]
        for i in range(1,n+1):
            if test_perfect_squares(i):
                dp.append(1)
            else:
                minNum = i # 设置的虚拟最大值
                for k in range(1,i//2+1):
                    minNum = min(dp[i-k]+dp[k],minNum)
                dp.append(minNum)
        # print(dp)
        return dp[-1]

# 优化了平方数的计算方式，改成预先计算出全部平方数
class Solution:
    def numSquares(self, n: int) -> int:
        squarelist = [i**2 for i in range(1,int(n**(0.5)+1))]
        # 动态规划，F(i) = min{ F(i-1)+F(1), F(i-2)+F(2), F(i-3)+F(3)...F(2)+F(i-2), F(1)+F(i-1) }
        dp = [0]
        for i in range(1,n+1):
            if i in squarelist:
                dp.append(1)
            else:
                minNum = i # 设置的虚拟最大值
                for k in range(1,i//2+1):
                    minNum = min(dp[i-k]+dp[k],minNum)
                dp.append(minNum)
        # print(dp)
        return dp[-1]