class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        num = 0
        # 手动依次计算出二进制对应的十进制
        for i in A:
            num = num * 2 + i
            if num % 5==0:
                res.append(True)
            else:
                res.append(False)
        return res