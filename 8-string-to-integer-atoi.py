class Solution:
    def myAtoi(self, str: str) -> int:
        numlist = ["0","1","2","3","4","5","6","7","8","9"]
        operator = ["+","-"]
        str = str.strip()
        if len(str) == 0:return 0 # 字符串仅包含空白字符，无法转换
        positiveFlag = True
        if str[0] not in numlist:
            if str[0] not in operator: # 既不是数字，也不是操作符
                return 0
            else:
                positiveFlag = str[0] == "+"  # 是操作符，判断是否为正数
                str = str[1:] # 去掉操作符
        if len(str) == 0 or str[0] not in numlist:return 0  # 字符串"+","-"，无法转换；字符串"+w"无法转换
        for i in range(len(str)):
            if str[i] not in numlist:
                i = i - 1#####
                break
        if positiveFlag:
            return min(int(str[:i+1]), 2**31-1)
        else:
            return max(-1*int(str[:i+1]), -1*(2**31))

