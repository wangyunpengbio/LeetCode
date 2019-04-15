class Solution:
    # 弹出和推入数字
    def reverse(self, x: int) -> int:
        result = 0
        while(x!=0):
            if x<0:
                pop = x % -10
            else:    
                pop = x % 10
            x = int(x / 10)
            result = result * 10 + pop
        if result < -2**31 or result > 2**31 -1: return(0)
        return result