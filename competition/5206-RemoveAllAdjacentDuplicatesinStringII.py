class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        recordStack = []
        for item in s:
            if len(recordStack) == 0:
                recordStack.append([item,1]) # recordStack记录“字符”及其“当前出现的数目”
            else:
                if item == recordStack[-1][0]: # 字符相同，出现数目+1
                    recordStack[-1][1] += 1
                else:
                    recordStack.append([item,1])  # 字符不同，新增一个字符
            while recordStack and recordStack[-1][1] == k:
                recordStack.pop()
        ans = ''
        for record in recordStack:
            ans = ans + record[0] * record[1]
        return ans