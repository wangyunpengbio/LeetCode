class Solution:
    # 动态规划 每个位置是，从头开始，在当前能获得的最大金额
    # 从第三位开始的转移方程是，当前位置的金额，加上隔一个位置，之前位置的最大值
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        if len(nums) == 1:return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,len(dp)):
            dp[i] = max(dp[:i-1]) + nums[i]
        return max(dp)