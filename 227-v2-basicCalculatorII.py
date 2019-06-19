class Solution:
#     一般需要符号栈、数据栈，两个。但是，看到网上一个写的不错的算法，只用了一个数据栈。符号栈用一个变量sign代替了，只存储上一个符号，主要思想如下：

#     将减法转化为加法（取相反数）

#     由于乘除法优先级高，直接计算

#     整数不仅一位，会>10

#     表达式中没有括号

#     注意：

#     加减乘除空格的ASCII码都小于'0'，ASCII对照表如下：http://tool.oschina.net/commons?type=4

#     先做减法，避免int溢出

#     char类型，不能使用switch
    def calculate(self, s: str) -> int:
        d = 0
        sign = "+"
        nums = []
        # 遍历字符串，把乘除全先计算好塞进去，减改成加
        for i in range(len(s)):
            if s[i] >= "0":
                d = d * 10 + ord(s[i]) - ord("0")
            if (s[i] < "0" and s[i] != " ") or i == len(s) - 1:
                if sign == "+":
                    nums.append(d)
                elif sign == "-":
                    nums.append(-d)
                elif sign == "*" or sign == "/":
                    # 如果是乘法，就弹出以后把两者的乘积塞回去，如果是除法，就弹出以后把两者的商塞回去
                    tmp = nums[-1] * d if sign == "*" else int(nums[-1] / d)
                    nums.pop()
                    nums.append(tmp)
                sign = s[i]
                d = 0
        # 把数据栈求和
        res = 0
        while len(nums) != 0:
            res = res + nums.pop()
        return res