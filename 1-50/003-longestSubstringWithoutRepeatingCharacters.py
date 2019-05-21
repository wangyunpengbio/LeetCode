class Solution:
    def testUnique(self,s:str):
        myset = set(s)
        if len(myset) != len(s):
            return False
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        # 暴力遍历全部子字符串
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.testUnique(s[i:j]): ans = max(ans,j-i)
        return ans 