class Solution:
    def mySqrt(self, x: int) -> int:
        # 逐个查找
        r = 1
        while r*r <= x:
            r = r + 1
        return r - 1