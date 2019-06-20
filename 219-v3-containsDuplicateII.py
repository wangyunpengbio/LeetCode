class Solution:
    # 用字典存储依次每个元素的位置，遇到每加入新的元素判断和之前位置的距离，距离小于k则属于重复
    # 如果重复就直接返回True，因为是从前到后遍历，所以如果较新的位置满足条件，之前的位置也肯定满足条件，直接更新即可元素位置即可，不用保存之前的位置
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                if i - dic[nums[i]] <= k:
                    return True
            dic[nums[i]] = i
        return False