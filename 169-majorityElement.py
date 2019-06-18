class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 开心消消乐，不一样的两个数相互抵消掉，剩下最后一个(或n)个数就是众数
        stack = []
        for item in nums:
            if len(stack) == 0:
                stack.append(item)
            else:
                if stack[-1] != item:
                    stack.pop()
                else:
                    stack.append(item)
        return stack[-1]