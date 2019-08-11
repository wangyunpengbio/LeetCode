class Solution:
    # 先计算闰年，再计算是哪儿天
    def ordinalOfDate(self, date: str) -> int:
        monthsRun = [31,29,31,30,31,30,31,31,30,31,30,31]
        monthsCommon = [31,28,31,30,31,30,31,31,30,31,30,31]
        datalist = [int(item) for item in date.split("-")]
        if (datalist[0] % 4 == 0 and datalist[0] % 100 != 0) or datalist[0] % 400 == 0:
            result = sum(monthsRun[:datalist[1]-1]) + datalist[2]
        else:
            result = sum(monthsCommon[:datalist[1]-1]) + datalist[2]
        return result