class Solution:
    # 双指针法
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums : return 0
        j = 0
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = nums[i]
        return j+1