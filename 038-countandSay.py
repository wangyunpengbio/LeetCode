class Solution:
    def countAndSay(self, n: int) -> str:
        a = "1#"
        # 依次生成就可以了
        for i in range(n-1):
            chartmp = a[0]
            starttmp = 0
            astrtmp = ""
            for index,char in enumerate(a):
                # print(index,char,chartmp,starttmp,astrtmp)
                if char != chartmp:
                    astrtmp = astrtmp+"".join([str(index - starttmp),chartmp])
                    starttmp = index
                    chartmp = char
            a = astrtmp + "#"
        return a[:-1]