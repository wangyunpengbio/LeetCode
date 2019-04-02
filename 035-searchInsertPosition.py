class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        middle = 0
        while l<r:
            middle = int((l+r)/2)
            if nums[middle] > target:
                r = middle - 1
            # 二分查找，由于middle会向下取一位，所以此处low必须＋1，而high不一定非要-1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
        if nums[l] >= target:
            return l
        elif nums[l] < target:
            return l + 1
