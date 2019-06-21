class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:return []
        res = []
        stack = [nums.pop(0)]
        while len(nums) != 0:
            item = nums.pop(0)
            if item != stack[-1] + 1:
                if len(stack) > 1: # 多个元素
                    res.append("->".join([str(stack[0]),str(stack[-1])]))
                else: # 单个元素
                    res.append(str(stack[0]))
                stack = []
            stack.append(item)
        # 栈里还剩下有元素
        if len(stack) > 1: # 多个元素
            res.append("->".join([str(stack[0]),str(stack[-1])]))
        else: # 单个元素
            res.append(str(stack[0]))
        return res