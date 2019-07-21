class Solution:
    # 直接两两比较 超时
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        dominoes = [sorted(domino) for domino in dominoes]
        for i in range(len(dominoes)-1):
            for j in range(i+1,len(dominoes)):
                if dominoes[i] == dominoes[j]:
                    res = res + 1
        return(res)