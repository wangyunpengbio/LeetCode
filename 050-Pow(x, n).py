class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 直接转化为累乘 Time Limit Exceeded (TLE)
        count = abs(n)
        res = 1
        for i in range(count):
            res = res * x
        res = res if n >0 else 1/res
        return res