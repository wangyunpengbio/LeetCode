class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 关键点：1、余数重复就开始了循环小数 2、负数先暂存符号，转成正数运算
        # 难点在于如何判断是否是循环小数，以及找出循环节的位置
        # 判断是循环: 跳出while循环的时候余数为0就不是循环小数
        # 找出循环节的位置: 当同一个余数出现两次时，就找到了循环节
        sign = '-' if numerator * denominator < 0 else ''
        numerator,denominator = abs(numerator),abs(denominator)
        quotient,remainder = divmod(numerator,denominator)
        if remainder == 0:
            return sign + str(quotient)
        else:
            integer = str(quotient)
        dic = {} # 键:余数 -> 值:出现余数的索引  余数重复就开始了循环小数
        decimal = ""
        i = 0
        while remainder != 0:
            dic[remainder] = i
            i = i + 1
            quotient,remainder = divmod(remainder * 10 ,denominator)
            decimal = decimal + str(quotient)
            if remainder in dic:
                decimal = decimal[:dic[remainder]] + "(" + decimal[dic[remainder]:] + ")"
                break
            # print(dic)
        return sign + integer + "." + decimal