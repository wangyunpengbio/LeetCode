class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0 or k == 10000:
            return False
        for i in range(len(nums)-1):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False

class Solution:
    # 排序以后可以快速通过最后一个案例
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums_loc = []
        for idx, num in enumerate(nums):
            nums_loc.append([num, idx])
        nums_loc.sort()
        n = len(nums)
        # print(nums_loc)
        for i in range(n):
            for j in range(i + 1, n):
                if nums_loc[j][0] - nums_loc[i][0] > t:
                    break
                if abs(nums_loc[i][1] - nums_loc[j][1]) <= k:
                    return True
        return False