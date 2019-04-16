class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = 0
        for i in range(len(nums)):
            # 在每个位置上,都计算之前跳到的最远位置能不能跳到当前位置
            if maxPos<i:
                return False
            # print(maxPos,nums[i]+i,i)
            # 如果能跳到当前位置,则在当前位置上,都计算能跳到的最远位置
            maxPos = max(nums[i]+i,maxPos)
            # 如果当前最大已经能跳到最后一个,则直接返回True,表示可以到达最后一个位置
            if maxPos>=len(nums)-1:
                return True
        return True