class Solution:
    # 根据题意找出递归公式即可
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u = 1,1,1,1,1
        for ite in range(n-1):
            atmp = i + e + u
            etmp = i + a
            itmp = o + e
            otmp = i
            utmp = i + o
            a = atmp
            e = etmp
            i = itmp
            o = otmp
            u = utmp
        return (a+e+i+o+u) % (10**9 + 7) # 防止数字过大，要根据题意取模（python里面表示 10^9+7 要写成10**9 + 7）