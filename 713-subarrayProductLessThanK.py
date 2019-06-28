class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        result = 0
        tempK = 1
        left,right = 0,0
        while left < N:
            # 一直移动right，直到出界或者子数组乘积不小于k
            while right < N and tempK * nums[right] < k:
                tempK *= nums[right]
                right += 1
            # 此时是特殊情况，需要修正两个指针，比如[10, 5, 1], k = 5,出现了比k大的元素，此时right无法移动，需要矫正
            if right <= left:
                left = left + 1
                right = left
                tempK = 1
            else:
                # 计算以nums[left]为左边界的子数组个数
                result += (right-left)
                tempK /= nums[left]
                left = left + 1
        return result