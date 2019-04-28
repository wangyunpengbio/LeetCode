class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法查找
        l,r = 1,x
        while l <= r:
            target = (l + r) // 2
            # print(l,r,target)
            if target * target > x:
                r = target
            elif target * target < x:
                l = target
            else: # 如果已经搜到，则直接返回结果
                return target
            if l + 1 == r and target == l: # 意思是如果已经卡住了，就像l,target,r= 2 2 3这样那么平方根的整数部分则为2
                return target
        # 如果输入为0，则输出为0
        return 0