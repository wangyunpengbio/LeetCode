class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(resultlist,result,arr):
            if len(arr) == 0:
                resultlist[0] = max(resultlist[0],len(result))
                return
            for i,item in enumerate(arr):
                if len(item) + len(result) != len(item|result): # 出现重复字符
                    dfs(resultlist,result,arr[i+1:])
                    return
                else:
                    dfs(resultlist,result|item,arr[i+1:])
        arrfilter = []
        # 先过滤掉有重复字符的子序列
        for item in arr:
            itemset = set(item)
            if len(item) == len(itemset):
                arrfilter.append(itemset)
        # 然后深度优先遍历
        resultlist = [0]
        dfs(resultlist,set(),arrfilter)
        return resultlist[0]