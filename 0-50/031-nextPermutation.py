class Solution:
    # 参考“题解”的思路，写出的答案
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右边开始找都是升序，找到第一个降序的数字位置 [i-1] < [i]
        i = len(nums) - 1
        while(i-1>=0):
            if nums[i-1] < nums[i]:
                break
            i = i - 1
        # 如果是全部降序，则直接给出下一个排列
        if i==0:
            nums[:] = nums[::-1]
            return None
        # 交换i-1和刚刚升序那串中第一个大于它的值  [j] > [i-1] > [j+1]
        # [i] > ... > [j+1] > [i-1] > [j]
        j = len(nums) - 1
        while(j > i-1):
            if nums[j] > nums[i-1]:
                break
            j = j - 1
        # print(i,j)
        nums[j],nums[i-1] = nums[i-1],nums[j]
        # 翻转i以后的数组
        nums[i:] = nums[i:][::-1]