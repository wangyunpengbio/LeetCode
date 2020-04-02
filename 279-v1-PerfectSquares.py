# 优化了平方数的计算方式，改成预先计算出全部平方数
# 递推公式优化：numSquares(n)=min(numSquares(n-k) + 1) ∀k∈square numbers
class Solution:
    def numSquares(self, n: int) -> int:
        squarelist = [i**2 for i in range(1,int(n**(0.5)+1))]
        dp = [0]
        for i in range(1,n+1):
            if i in squarelist:
                dp.append(1)
            else:
                minNum = i # 设置的虚拟最大值
                for k in squarelist:
                    if i < k:
                        break
                    minNum = min(dp[i-k]+1,minNum)
                dp.append(minNum)
        # print(dp)
        return dp[-1]