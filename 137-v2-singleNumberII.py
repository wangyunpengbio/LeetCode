class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 将数组(用set去重后求和的三倍 - 原有数组)÷2即为结果
        return int((3*sum(set(nums)) - sum(nums))/2)
    
