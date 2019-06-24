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
        # 先求出山脉的山顶点
        left,right = 0,n-1
        middle = int((right+left)/2)
        middleValue = mountain_arr.get(middle)
        middleValueLeft = mountain_arr.get(middle-1)
        middleValueRight = mountain_arr.get(middle+1)
        while middleValueLeft < middleValue < middleValueRight or middleValueLeft > middleValue > middleValueRight:
            # print(left,middle,right)
            if middleValueLeft < middleValue < middleValueRight:
                left = middle + 1
            if middleValueLeft > middleValue > middleValueRight:
                right = middle - 1
            middle = int((right+left)/2)
            # print(left,middle,right)
            middleValue = mountain_arr.get(middle)
            if middle-1<0:
                middleValueLeft = mountain_arr.get(middle)
            else:
                middleValueLeft = mountain_arr.get(middle-1)
            if middle+1>n-1:
                middleValueRight = mountain_arr.get(middle)
            else:
                middleValueRight = mountain_arr.get(middle+1)
        # 修补bug，如果山顶是第二个元素
        if mountain_arr.get(0)<mountain_arr.get(1) and mountain_arr.get(1)>mountain_arr.get(2):
            middle = 1
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