class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        last = []
        # 依次计算并保留每一位置各种长度子序的和 Time Limit Exceeded (TLE)
        for i in range(len(nums)):
            current = [item + nums[i] for item in last]
            current.append(nums[i])
            res = max(res,max(current))
            last = current
            # print(current)
        return res