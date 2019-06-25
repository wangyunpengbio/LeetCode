class Solution:
    # 首先在两侧加上山底，防止单调递增的数组报错
    # 找山峰也是用二分查找，理念是，如果该处向右是递增的，则山顶在右侧；如果该处向左是递增的，则山顶在左侧
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,float("-inf"))
        nums.append(float("-inf"))
        N = len(nums)
        left,right = 0,N-1
        while left <= right:
            middle = (left + right)//2
            # print(left,right,middle)
            # print(nums[left],nums[right],nums[middle])
            # print("---")
            if nums[middle] < nums[middle+1]:
                left = middle + 1
            else:
                right = middle - 1
        # print(left,right,middle)
        return left - 1  # 此处返回left是经过一系列debug出来的