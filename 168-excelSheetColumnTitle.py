class Solution:
    def convertToTitle(self, n: int) -> str:
        # 要减1，现实中第一个是逻辑上的1，计算机里第一却是0
        res = ""
        while n > 0:
            n,current = divmod(n-1,26)
            res = chr(current + ord("A")) + res
        if n != 0:
            res = chr(n-1 + ord("A")) + res
        return res
