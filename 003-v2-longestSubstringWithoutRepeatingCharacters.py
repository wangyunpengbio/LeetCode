class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 参考答案的滑动窗口方法，用双指针来进行滑动
        n = len(s)
        myset = set()
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in myset:
                myset.add(s[j])
                j = j + 1
                ans = max(ans,j-i)
            else:
                myset.remove(s[i])
                i = i + 1
        return ans