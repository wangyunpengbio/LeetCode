class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        if len(nums)==0:
            return [-1,-1]
        start,end = 0,len(nums) - 1
        # 二分查找最终都是start==end
        while start < end:
            mid = int((start+end)/2)
            # 直到start变成第一个target
            if(nums[mid]<target):
                start = mid + 1
            # 上面条件无等号，end变成target无所谓
            else:
                end = mid
        if nums[start]!=target:
            return [-1,-1]
        else:
            result[0] = start
        end = len(nums) -1
        # 二分查找最终都是start==end
        while start < end:
            mid = int((start+end+1)/2)
            # 此处条件有等号，start变成target无所谓
            if(nums[mid]<=target):
                start = mid
            # 直到end变成最后一个target
            else:
                end = mid - 1
        result[1] = start
        return result
