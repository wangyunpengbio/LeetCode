class Solution:
    # 滑动窗口,双指针
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s > sum(nums):return 0
        N = len(nums)
        left, right, res, sum_lr = 0, 0, N + 1, 0 # 双指针都从第一位出发
        while right < N:
            while sum_lr < s and right < N:   # sum_lr小则右指针右移
                sum_lr = sum_lr + nums[right]
                right = right + 1
            while sum_lr >= s and left >= 0:  # sum_lr大则左指针右移
                res = min(res,right-left)
                sum_lr = sum_lr - nums[left]
                left = left + 1
        return res