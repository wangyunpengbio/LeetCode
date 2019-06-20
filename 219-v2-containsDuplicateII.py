class Solution:
    # 超时
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 直接把对应元素前后k个元素拿出来比较
        for i in range(len(nums)):
            if nums[i] in nums[max(0,i-k):i] or nums[i] in nums[i+1:i+k+1]:
                return True
        return False

class Solution:
    # 超时
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 直接比较后k个元素拿出来比较即可
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False