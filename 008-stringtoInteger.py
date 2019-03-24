class Solution:
    def myAtoi(self, st: str) -> int:
        if st == "": return 0
        # 如果前面有奇怪的字符，且字符不是空格 直接返回0
        first = ord(st[0])
        if (first > 57 or first < 48) and st[0] != " " \
        and st[0] != "+" and st[0] != "-": return 0
        # 把前端的空格全部去掉
        for i in range(len(st)):
            if st[i] != " ":
                st = st[i:]
                break
        # flag表示正负,正数为1 负数为-1,去除掉前面的正负号
        flag = 1
        if st[0]=="-":
            flag = -1
            st = st[1:]
        elif st[0]=="+":
            st = st[1:]
        # 最后处理干净的字符串转成数值
        result = 0
        for i in range(len(st)):
            if 48 <= ord(st[i]) <= 57:
                result = result * 10 + int(st[i])
            else:
                break
        # 计算最终数值
        result = result*flag
        if result <-2**31:
            return(-2**31)
        elif result > 2**31-1:
             return(2**31-1)
        return(result)