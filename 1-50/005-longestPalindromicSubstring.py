class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        res = ""
        # 暴力遍历全部子字符串
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j][::-1] == s[i:j] and j-i > ans:
                    ans = max(ans,j-i)
                    res = s[i:j]
        return res
        