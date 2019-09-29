class Solution:
    # 直接挨个找最长序列，会超时
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costlist = []
        for i in range(len(s)):
            currentCost = abs(ord(s[i]) - ord(t[i]))
            costlist.append(currentCost)
        res = 0
        for i in range(len(costlist)):
            curLen = 1
            curSum = costlist[i]
            if curSum > maxCost:
                continue
            res = max(res,curLen)
            for j in range(i+1,len(costlist)):
                curLen += 1
                curSum += costlist[j]
                if curSum > maxCost: break
                res = max(res,curLen)
        return res
class Solution:
    # 解答错误，这不是背包问题，背包问题物体是可以间隔着拿，这题字符必须挨着拿
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costlist = []
        for i in range(len(s)):
            currentCost = abs(ord(s[i]) - ord(t[i]))
            costlist.append(currentCost)
        n = len(costlist)
        f = [[0 for j in range(maxCost+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, maxCost+1):
                f[i][j] = f[i-1][j]
                if j >= costlist[i-1] and f[i][j] < f[i-1][j-costlist[i-1]] + 1:
                    f[i][j] = f[i-1][j-costlist[i-1]] + 1
        return(f[-1][-1])