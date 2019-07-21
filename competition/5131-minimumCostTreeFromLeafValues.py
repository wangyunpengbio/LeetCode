class Solution:
    # 深度优先遍历 超时
    def mctFromLeafValues(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            arr[i] = [arr[i],0]
        def dfs(results,arr):
            if len(arr) == 1:
                results.append(arr[0][1])
            else:
                for i in range(len(arr)-1):
                    item = [None,None]
                    item[0] = max(arr[i][0], arr[i+1][0])
                    item[1] = arr[i][1] + arr[i+1][1] + arr[i][0] * arr[i+1][0]
                    dfs(results,arr[:i]+[item]+arr[i+2:])
        results = []
        dfs(results,arr)
        return min(results)
