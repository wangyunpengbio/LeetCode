class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        res = ""
        remainder = 0
        # 先把两者长度可以和在一起的加起来
        for i in range(0,min(len_a,len_b)):
            current,remainder = divmod(int(a[len_a - i - 1]) + int(b[len_b - i - 1]) + remainder, 2)
            res = str(remainder) + res
            remainder = current
        # 再把剩下的加起来
        if len_a > len_b:
            for i in range(min(len_a,len_b),len_a):
                current,remainder = divmod(int(a[len_a - i - 1]) + remainder, 2)
                res = str(remainder) + res
                remainder = current
        else:
            for i in range(min(len_a,len_b),len_b):
                current,remainder = divmod(int(b[len_b - i - 1]) + remainder, 2)
                res = str(remainder) + res
                remainder = current
        # 最后把多的那个加上
        if remainder == 1:
            res = str(remainder) + res
        return res