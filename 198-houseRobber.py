class Solution:
    # 深度优先遍历，找出所有可能
    def rob(self, nums: List[int]) -> int:
        def dfs(results,result,nums):
            results[0] = max(results[0],result)
            for i in range(len(nums)):
                dfs(results,result+nums[i],nums[i+2:])
        results = [0]
        dfs(results,0,nums)
        return results[0]