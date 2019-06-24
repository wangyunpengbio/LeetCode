class Solution:
    # 超时 暴力法
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        for i in range(m+1,n+1):
            res = res & i
        return res