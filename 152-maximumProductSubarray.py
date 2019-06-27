class Solution:
    # 超时 先用把连续正数都给乘起来把数组变小，再暴力遍历全部可能情况
    def maxProduct(self, nums: List[int]) -> int:
        # 计算数组的乘积
        def calculateProduct(nums):
            res = 1
            for item in nums:
                res = res * item
            return res
        stack = []
        N = len(nums)
        i = 0
        while i < N:
            item = nums.pop(0)
            if item > 0:
                stack.append(item)
            else:
                if len(stack) != 0:
                    nums.append(calculateProduct(stack))
                nums.append(item)
                stack = []
            i = i + 1
        if len(stack) != 0:
            nums.append(calculateProduct(stack))
        result = float("-inf")
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                result = max(result,calculateProduct(nums[i:j+1]))
        return result