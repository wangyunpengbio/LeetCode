class Solution:
    # 超时 暴力遍历全部买卖的点
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            # 小优化的if语句，如果后一天股票跌了，就肯定不是在后一天卖，直接跳过
            if prices[i] > prices[i+1]:
                continue
            for j in range(i+1,len(prices)):
                res = max(res,prices[j]-prices[i])
        return res