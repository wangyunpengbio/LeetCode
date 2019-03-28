# 双指针法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 4: return res
        for a in range(0,len(nums)-3):
            # 首个a值无条件进入循环，后边的or条件是去除a的重复。
            if a == 0 or nums[a] > nums[a-1]:
                for b in range(a + 1,len(nums)-2):
                    # 首个b值无条件进入循环，后边的or条件是去除b的重复。
                    if b == a + 1 or nums[b] > nums[b-1]:
                        c = b + 1
                        d = len(nums) - 1
                        while c < d:
                            s = nums[a] + nums[b] + nums[c] + nums[d]
                            if s == target:
                                res.append([nums[a],nums[b],nums[c],nums[d]])
                                c +=1
                                d -=1
                                # 后边的and条件是去除c的重复。
                                while c < d and nums[c] == nums[c-1]:
                                    c += 1
                                # 后边的and条件是去除d的重复。
                                while c < d and nums[d] == nums[d+1]:
                                    d -= 1
                            elif s > target:
                                d -=1
                            else :
                                c +=1
        return res