class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = abs(n)
        res = 1
        while count:
            if count % 2 == 1:
                res = res * x
            x = x * x
            count = count // 2
        res = res if n >0 else 1/res
        return res