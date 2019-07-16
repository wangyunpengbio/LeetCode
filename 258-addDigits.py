class Solution:
    # 暴力法
    def addDigits(self, num: int) -> int:
        def calculateDigitSum(num):
            i = 0
            while num // 10 != 0:
                current,num = divmod(num,10)
                i = i + current
            return i + num
        while num // 10 != 0:
            num = calculateDigitSum(num)
        return num