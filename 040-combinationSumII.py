class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 深度优先搜索，结果列表在函数间传递，可以直接追加
        def dfs(results,result,candidates,target,level):
            if target == 0:
                # print(result,results)
                # 此处需要生成新的列表，以避免与之前的操作互相影响
                tmp = list(result)
                tmp.sort()
                # print(result not in results)
                if tmp not in results:
                    results.append(tmp)
                    # print(results)
            elif target > 0:
                for i in range(level,len(candidates)):
                    result.append(candidates[i])
                    leftcandidates = candidates[:i] + candidates[i+1:]
                    # print(leftcandidates,result,results,target,target-candidates[i])
                    dfs(results,result,leftcandidates,target-candidates[i],i)
                    result.pop()
        results = []
        dfs(results,[],candidates,target,0)
        return results