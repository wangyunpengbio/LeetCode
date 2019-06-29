class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if nums[0] < nums[-1]: # 如果没有旋转，则直接返回第一个值，由于下面的二分查找是基于左右顶端的值，所以此处去掉会有bug
            return nums[0]
        # 很常规的思路，中间比最左端值大，区间左端向右移；中间值比最右端值小，区间右端向左移
        # 当然，很有必要的是，如果查找到最小值，直接返回（更高效，并且非常必要）
        # 如果区间左端和中间值重合，则会死循环，直接break
        left,right = 0,N-1
        while left <= right:
            middle = int((left+right)/2)
            # print(left,middle,right)
            if nums[middle] > nums[0]:
                left = middle + 1
            if nums[middle] < nums[-1]:
                right = middle - 1
            if nums[middle-1] > nums[middle]:
                return nums[middle]
            if middle == left:break
        # print(left,middle,right)
        # 最后结果一般就在left,middle,right之间，直接判断即可
        return min(nums[left],nums[middle],nums[right])