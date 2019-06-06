class Solution:
    # 动态规划
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
# 用一个数组res来存状态，False代表以当前索引对应的字符为结尾的字符串不可被完全拆分，True代表可以拆分。
# 之后遍历字符串的每个字符，对于每个字符，用一个指针p向前找距离在maxlen以内的字符串，当满足以下两个条件，即说明以当前字符结尾的字符串是可以被拆分的：

# p指向的位置的状态是True（说明0到p的字符串是可以完全拆分的），且s[p+1:i]在字典里面
# p指向的位置的状态是字符串的开头，即s[0:i+1]在字典里面
        res = [False] * len(s)
        for i in range(len(res)):
            p = i
            while p >= 0:
                if (res[p] == True and s[p+1:i+1] in wordDict) or (s[0:i+1] in wordDict):
                    res[i] = True
                    break
                p = p - 1
        return res[-1]