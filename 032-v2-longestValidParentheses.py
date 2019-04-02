class Solution:
    # 直接弄一个数组记录匹配上的括号的位置，
    # 0代表对应位置括号没有对应的，
    # 1表示对应位置括号有对应的
    # 在栈遍历的时候顺便把这个数组弄好，然后找出最长的连续“1”即可
    def longestValidParentheses(self, s: str) -> int:
        boollist = [0 for i in range(len(s))]
        stack = []
        for index,char in enumerate(s):
            if char == ")":
                top = stack.pop() if stack else ["",""]
                if top[1] =="(":
                    boollist[index] = 1
                    boollist[top[0]] = 1
            else:
                stack.append([index,char]) # 遇到"(",直接压入栈，并且记录位置
        # print(boollist)
        maxlen = 0
        tmplen = 0
        flag = False
        for item in boollist:
            if item == 1:
                tmplen = tmplen + 1
                flag = True
            else:
                tmplen = 0
                flag = False
            if flag:
                maxlen = max(maxlen,tmplen)
        return maxlen