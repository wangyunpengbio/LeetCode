class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res =[]
        i = 0
        closestNum = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            # 双指针法，两者依次向前向后遍历
            while j < k:
                ourSum = sum((nums[i],nums[j],nums[k]))
                if abs(ourSum-target) < abs(closestNum-target):
                    closestNum = ourSum
                if ourSum > target:
                    k = k - 1
                elif ourSum < target:
                    j = j + 1
                else :
                    # 如果已经等于target的话，直接返回
                    return target
        return closestNum
