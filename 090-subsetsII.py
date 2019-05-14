class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 深度优先搜索 跟78题一样，不过多了一个排序
        def dfs(results,result,nums,level):
            if result not in results:
                results.append(result[:])
            for i,item in enumerate(nums[level:]):
                result.append(item)
                dfs(results,result,nums,level=level+i+1) # 加i是为了获得数组的绝对位置 不然也可以  dfs(results,result,nums[i:],level=level+1)
                result.pop()
        results = []
        nums.sort() # 先排序
        dfs(results,[],nums,level=0)
        return(results)