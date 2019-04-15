class Solution:
    # 其实是N型的顺序
    # 按行访问
    def convert(self, s: str, numRows: int) -> str:
        cycleLen = 2 * numRows - 2
        res = ""
        if len(s) < numRows or numRows == 1: return s
        # 第一行
        for i in range(0,len(s),cycleLen):
            res = res + s[i]
        # 中间多行
        for h in range(1,numRows - 1):
            for j in range(0,len(s) + cycleLen,cycleLen):
                if 0 < j - h < len(s):
                    res = res + s[j - h]
                if 0 < j + h < len(s):
                    res = res + s[j + h]
        # 最后一行
        for z in range(0,len(s),cycleLen):
            if numRows - 1 + z < len(s):
                res = res + s[numRows - 1 + z]
        return res
        