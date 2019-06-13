class Solution:
    # 分类讨论 打家劫舍 I
    # 动态规划 每个位置是，从头开始，到打劫当前家，能获得的最大金额
    # 从第三位开始的转移方程是，当前位置的金额，+ 加上隔一个位置，之前位置的最大值
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        if len(nums) == 1:return nums[0]
        if len(nums) == 2:return max(nums[0],nums[1])
        # 打劫第一个，不打劫最后一个
        n = len(nums)
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = nums[1]
        for i in range(2,n-1):
            dp1[i] = max(dp1[:i-1]) + nums[i]
        # 不打劫第一个，打劫最后一个
        dp2 = [0] * len(nums)
        dp2[0] = 0 # 不打结第一个
        dp2[1] = nums[1]
        for i in range(2,n):
            dp2[i] = max(dp2[:i-1]) + nums[i]
        # print(dp1,dp2)
        return max(dp1+dp2) # 两个dp数组连起来，最大值