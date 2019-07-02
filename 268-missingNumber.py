# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         N = len(nums)
#         rawSum = (0 + N) * (N+1) / 2
#         for item in nums:
#             rawSum = rawSum - item
#         return int(rawSum)
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing = missing ^ i ^ num
        return missing

