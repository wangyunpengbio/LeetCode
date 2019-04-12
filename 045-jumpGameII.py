class Solution:
    # 深度优先搜索 超出时间限制 Time Limit Exceeded (TLE)
    def jump(self, nums: List[int]) -> int:
        def dfs(currentPos,count,nums,res):
            # 如果已经跳到最后一个元素，则追加该结果
            if currentPos >= len(nums)-1:
                res.append(count)
            else:
                for i in range(1,nums[currentPos] + 1):
                    pos = i + currentPos
                    dfs(currentPos = pos,count = count + 1,nums = nums,res = res)
        res = []
        dfs(currentPos = 0,count = 0,nums = nums,res = res)
        return(min(res))