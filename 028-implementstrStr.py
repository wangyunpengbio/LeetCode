class Solution:
    # 直接暴力遍历 
    '''可以像KMP算法优化'''
    def strStr(self, haystack: str, needle: str) -> int:
        targetlen = len(needle)
        for i in range(len(haystack)-targetlen+1):
            if haystack[i:targetlen+i]==needle:
                return i
        return -1