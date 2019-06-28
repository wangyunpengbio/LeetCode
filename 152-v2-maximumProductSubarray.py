class Solution:
    # 动态规划
    # 遍历数组时计算当前最大值，不断更新
    # 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
    # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
    # 当负数出现时则imax与imin进行交换再进行下一步计算
    # 时间复杂度：O(n)O(n)
    def maxProduct(self, nums: List[int]) -> int:
        # 令imax为包含当前元素的当前最大值
        N = len(nums)
        imax,imin,result = nums[0],nums[0],nums[0]
        for i in range(1,N):
            if nums[i] < 0:imax,imin = imin,imax
            imax = max(nums[i],nums[i]*imax)
            imin = min(nums[i],nums[i]*imin)
            result = max(imax,result)
        return result