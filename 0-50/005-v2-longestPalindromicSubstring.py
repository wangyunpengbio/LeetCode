class Solution:
    # 中心扩展算法
    def expandAroundCenter(self, s, left, right):
        L,R = left,right
        while L>=0 and R<len(s) and s[L]==s[R]:
            L = L - 1
            R = R + 1
        return R - L - 1
    def longestPalindrome(self, s: str) -> str:
        res = ""
        start,end = 0,0
        for i in range(0,len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            lenRes = max(len1,len2)
            if lenRes > end - start:
                start = i - int((lenRes - 1)/2)
                end = i + int(lenRes/2)
        return s[start:end+1]
        