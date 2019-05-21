class Solution:
    # 直接列表翻转
    def reverse(self, x: int) -> int:
        s = list(str(x))
        s.reverse()
        if x < 0:
            s.pop()
            s.insert(0,"-")
        res = int(''.join(s))
        if res < -2**31 or res > 2**31 -1: return(0)
        return(res)