class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        resultlist = []
        numlist = list(num)
        left = len(numlist) - k
        # 深度优先搜索，找出所有的数字
        def dfs(resultlist,result,numlist,left):
            if len(result) == left:
                if left == 0: 
                    resultlist.append(0)
                else:
                    resultlist.append(int("".join(result)))
            for i in range(len(numlist)):
                result.append(numlist[i])
                dfs(resultlist,result,numlist[i+1:],left)
                result.pop()
        dfs(resultlist,[],numlist,left)
        # print(resultlist)
        return str(min(resultlist))
        