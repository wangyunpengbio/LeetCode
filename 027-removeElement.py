class Solution:
    # 直接删掉列表中的对应元素
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        rawlen = len(nums)
        while i <len(nums):
            if nums[i] == val:
                j = j + 1
                del nums[i]
                i = i - 1
            i = i + 1
        return rawlen - j