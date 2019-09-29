class Solution:
    # 找连续字符串的最长，使用双指针
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # costlist记录每个字符转换的代价
        costlist = []
        for i in range(len(s)):
            currentCost = abs(ord(s[i]) - ord(t[i]))
            costlist.append(currentCost)
        print(costlist)
        res = 0
        l,r = 0,0
        currentCost = 0
        while l < len(costlist) and r < len(costlist):
            currentCost += costlist[r]
            while currentCost > maxCost:
                currentCost -= costlist[l]
                l = l + 1
            print(l,r)
            res = max(res,r - l + 1)
            r = r + 1
        return res