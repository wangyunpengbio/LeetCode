class Solution:
    # 超时
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 如果k距离比数组要大，则单独判断
        if len(nums) <= k:return len(set(nums)) != len(nums)
        for i in range(len(nums)-k):
            # 滑动窗口判断窗口内是否有重复元素
            if len(set(nums[i:i+k+1])) != k+1:
                return True
        return False