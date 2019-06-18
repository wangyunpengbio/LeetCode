class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 先排序，再取正中间的值
        nums.sort()
        return nums[len(nums)//2]