class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 深度优先搜索，结果列表在函数间传递，可以直接追加
        def dfs(results,result,candidates,target,level):
            if target == 0:
                # print(result)
                results.append(list(result))
            elif target > 0:
                for i in range(level,len(candidates)):
                    result.append(candidates[i])
                    dfs(results,result,candidates,target-candidates[i],i)
                    result.pop()
        results = []
        dfs(results,[],candidates,target,0)
        return results