# 1.将数组排序 2.定义三个指针，i，j，k。遍历i，那么这个问题就可以转化为在i之后的数组中寻找nums[j]+nums[k]=-nums[i]这个问题，也就将三数之和问题转变为二数之和---（可以使用双指针）
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            # 首个i值无条件进入循环，后边的or条件是去除i的重复。
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                # 双指针遍历
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        # 后边的or条件是去除l的重复。
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        # 后边的and条件是去除l的重复。
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res