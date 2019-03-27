# 超出时间限制
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 直接暴力求出所有三数组合的和
        ourSumRes = 0
        if len(nums) < 3: return ourSumRes
        # 先计算前三个数字的和与目标之间的距离
        ourDistance = abs(sum(nums[:3]) - target)
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    ourSumtmp = sum((nums[i],nums[j],nums[k]))
                    ourDistancetmp = abs(ourSumtmp - target)
                    if ourDistance >= ourDistancetmp:
                        ourDistance = ourDistancetmp
                        ourSumRes = ourSumtmp
        return ourSumRes