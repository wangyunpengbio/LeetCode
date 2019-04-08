# 题目的意思是射击，遇到回文可以消一串回文，问最少射击几次
# 比如[1,2,3]这个数组射击3次消完
# 比如[1,2,3,2]这个数组射击2次消完，先打2 3 2算一次，再消掉1算一次
# 比如[1,2,4,5,2,1]这个数组射击2次消完，先打4或者5算一次，剩下的变成回文数，再一次消完

def expandAroundCenter(s, left, right):
    L,R = left,right
    while L>=0 and R<len(s) and s[L]==s[R]:
        L = L - 1
        R = R + 1
    return (L,R)
def palindrome(s):
    recordlist = [0]*len(s)
    for i in range(0,len(s)):
#         print(recordlist)
        (L,R) = expandAroundCenter(s,i,i)
#         print(L,R)
        # 至少要成功左右分开过一次
        if R - L !=2:
            for i in range(len(recordlist)):
                if L<i<R:
                    recordlist[i]=1
        (L,R) = expandAroundCenter(s,i,i+1)
#         print(L,R)
        # 至少要成功左右分开过一次
        if R - L !=1:
            for i in range(len(recordlist)):
                if L<i<R:
                    recordlist[i]=1
    return recordlist
def dfs(nums,result,level):
    if len(nums)==0:
        result.append(level)
        return
    level = level + 1
    i = 0
    while i < len(nums):
        recordlist = palindrome(nums)
        start = end = i
#         print(recordlist,i,recordlist[start])
        while start >=0 and recordlist[start]==1:
            start = start - 1
        start = start + 1
        while end <len(recordlist) and recordlist[end]==1:
            end = end + 1
        end = end - 1
#         print("---",nums,start,end,recordlist,level,"---")
        if start - end == 2:
            numsleft = nums[0:i]+nums[i+1:]
            if len(numsleft) !=0:
#                 print(i,nums,numsleft,start,end,recordlist,level)
                dfs(numsleft,result,level)
            else:
#                 print("Append",i,nums,numsleft,start,end,recordlist,level)
                result.append(level)
                return
        else:
            numsleft = nums[0:start]+nums[end+1:]
#             print(nums,numsleft,start,end,recordlist,level)
            dfs(numsleft,result,level)
        i = i + 1
result = []
nums = [1,4,2,1]
dfs(nums,result,0)