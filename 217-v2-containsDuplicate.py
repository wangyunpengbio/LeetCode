class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for item in nums:
            if item in dic.keys():
                return True
            dic[item] = 1
        return False