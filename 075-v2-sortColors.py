class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法三：基于三路快排的partition的解法，时间复杂度O(n)，只需要一边遍历
        # https://www.imooc.com/article/16141
        i = 0  # nums[0..<i) == 0
        j = 0  # nums[i..<j) == 1
        k = len(nums)# nums[k..<n) == 2
        while(j < k):
            if(nums[j] == 1):
                j = j + 1
            elif(nums[j] == 0):
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j + 1
            else:
                nums[j],nums[k - 1] = nums[k - 1],nums[j]
                k = k - 1
