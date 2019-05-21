class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0,count1,count2 = 0,0,0
        for item in nums:
            if item == 0:
                count0 = count0 + 1
            elif item == 1:
                count1 = count1 + 1
            else:
                count2 = count2 + 1
        nums[:] = [0] * count0 + [1] * count1 + [2] * count2