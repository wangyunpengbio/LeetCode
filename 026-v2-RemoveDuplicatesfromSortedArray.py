class Solution:
    # 自己想出来的用栈结构，可以存储去除重复数据后的数组
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums : return 0
        stack = []
        j = 0
        for i in range(1,len(nums)):
            stack.append(nums[i])
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = stack.pop()
        return j+1