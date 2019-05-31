class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: # 输入数组为空则直接返回0
            return 0
        profit = 0
        minToNow = prices[0]
        # minToNow记录到当前为止的最小价格，最大利润为:max(之前的最大利润 or 当前天的价格-到目前为止的最小价格)
        for i in range(len(prices)):
            profit = max(profit,prices[i]-minToNow)
            minToNow = min(minToNow,prices[i])
        return profit