class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or len(strs[0])==0:return("")
        i = 0
        # 纵向扫描：从下标0开始，判断每一个字符串的下标0，判断是否全部相同。直到遇到不全部相同的下标。时间性能为O(n*m)。
        flag = True
        while flag:
            for singleStr in strs:
                if i != len(singleStr) and singleStr[i] == strs[0][i]:
                    continue
                else:
                    flag = False
                    break
            i = i + 1
        return strs[0][0:i-1]