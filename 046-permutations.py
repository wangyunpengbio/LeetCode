class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 深度优先搜索
        def dfs(results,result,nums):
            # 如果没有元素剩下，则遍历完成
            if len(nums)==0:
                results.append(result[:])
                # print(results)
                return
            else:
                for i in range(len(nums)):
                    left = nums[:i] + nums[i+1:]
                    result.append(nums[i])
                    dfs(results,result,left)
                    result.pop() # 这个pop很重要，这次遍历完成，把刚刚加进去的那个元素弹出，给下一个元素挪位置
        results = []   
        dfs(results,[],nums)
        return results