class Solution:
    # 逐个数字检验，搜索范围太大，会超时
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def testNum(num):
            if 0 <= num <= 10:
                return True
            else:
                num, tmp = divmod(num,10)
                while num > 0:
                    num, current = divmod(num,10)
                    if abs(tmp-current) != 1:
                        return False
                    else:
                        tmp = current
                return True
        result = []
        for i in range(low,high+1):
            if testNum(i):
                result.append(i)
        return result