class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end,mid = 0,len(nums)-1,0
        while start + 1 < end: # 移动到最后start和end没重合
            mid = int((start+end)/2)
            # print(start,end,mid)
            if nums[start] <= nums[mid]:
                start = mid
            else:
                end = mid
        return min(nums[0],nums[start],nums[end]) # nums[0]防止数组升序没有翻转