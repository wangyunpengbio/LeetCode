# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 得到数组长度
        n = mountain_arr.length()
        # 优化版本 先求出山脉的山顶点
        left,right = 0,n-1
        while left <= right :
            middle = int((right+left)/2)
            middleValue = mountain_arr.get(middle)
            middleValueRight = mountain_arr.get(middle+1)
            if middleValue < middleValueRight:
                left = middle + 1
            else:
                right = middle - 1
        # 二分查找山顶左侧
        top = middle
        left,right = 0,top
        while left <= right:
            mid = (left + right) // 2
            middleValue = mountain_arr.get(mid)
            if middleValue > target:
                right = mid - 1
            elif middleValue < target:
                left = mid + 1
            else:
                return mid
        # 二分查找山顶右侧
        left,right = top,n-1
        while left <= right:
            mid = (left + right) // 2
            middleValue = mountain_arr.get(mid)
            if middleValue > target:
                left = mid + 1
            elif middleValue < target:
                right = mid - 1
            else:
                return mid
        return -1