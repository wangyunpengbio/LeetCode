class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        递归
        n分为奇偶数两种情况
        """
        if not n:
            return 1
        if n < 0 :
            return 1/self.myPow(x, -n)
        if n % 2:
            # n为奇数的情况
            return self.myPow(x, n-1) * x
        return self.myPow(x * x, n / 2)