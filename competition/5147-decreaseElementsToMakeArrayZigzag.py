class Solution:
    # 直接按照题意算即可，分别算出奇数和偶数锯齿状所需步数
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1]) + 1
        def calSmall(left,middle,right):
            target = min(left,right)
            current = (middle - target + 1) if middle >= target else 0
            return current
        reseven = 0
        for i in range(1,len(nums),2):
            if i + 1 < len(nums):
                reseven += calSmall(nums[i-1],nums[i],nums[i+1])
            else:
                reseven += calSmall(nums[i-1],nums[i],float("inf"))
        resodd = 0
        for i in range(0,len(nums),2):
            if i != 0 and i + 1 != len(nums):
                resodd += calSmall(nums[i-1],nums[i],nums[i+1])
            elif i == 0:
                resodd += calSmall(float("inf"),nums[i],nums[i+1])
            else:
                resodd += calSmall(nums[i-1],nums[i],float("inf"))
        return min(reseven,resodd)