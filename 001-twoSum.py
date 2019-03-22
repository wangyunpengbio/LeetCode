class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # 一遍哈希，边存边找
        for i,item in enumerate(nums):
            other = target - item
            if other in hashmap:
                return [hashmap[other],i]
            hashmap[item] = i
        return None